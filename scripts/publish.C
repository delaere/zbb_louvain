#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <TDirectory.h>
#include <TFile.h>
#include <TH1.h>
#include <TROOT.h>
#include <TSystem.h>
#include <TCanvas.h>
#include <THStack.h>
#include <TList.h>
#include <TKey.h>
#include <TStyle.h>
#include <TLegend.h>

class wwwPublisher
{
  public:
    wwwPublisher():menuCreated(false),menu(NULL) {}
    ~wwwPublisher() {}
    void traverseDir(TDirectory* datadir, const char* outpath);
    void createFrames(const char* path);
    void addMenuFooter();
  private:
    void dumpHisto(TCanvas* h,const char* outpath);
    void createMenuHeader(const char* path);
    void addMenuItem(const char* name, const char* path);
    void closeMenuItem();
    bool menuCreated;
    ofstream* menu;
    string basepath;
};

void wwwPublisher::traverseDir(TDirectory* datadir, const char* outpath)
{
   std::cout << "processing " << datadir->GetName() << std::endl;
   if(gSystem->mkdir(outpath)==-1) {
     std::cout << "Error: directory " << outpath << " already exists or could not be created." << std::endl;
     return;
   }
   addMenuItem(datadir->GetName(), outpath);
   char buffer[1024];

   TList* keys = datadir->GetListOfKeys();
   TIter next(keys);
   TKey *key;
   while ((key = (TKey*) next())) {
     if(key->IsFolder()) {
        sprintf(buffer,"%s/%s",outpath,key->GetName());
        traverseDir((TDirectory*)key->ReadObj(),buffer);
     } else if (key->ReadObj()->InheritsFrom("TCanvas")) {
        dumpHisto((TCanvas*)key->ReadObj(),outpath);
     } else if (key->ReadObj()->InheritsFrom("TH1")) { 
        TCanvas* c = new TCanvas;
        TH1* h = (TH1*)key->ReadObj();
        h->Draw();
        dumpHisto(c,outpath);
        delete c;
     }
   }
   closeMenuItem();
   //call diow.pl
   sprintf(buffer,"cd %s;%s/src/UserCode/zbb_louvain/scripts/diow.pl -o diow.html -c 4 ",
           outpath,gSystem->Getenv("CMSSW_BASE"));
   std::cout << "will run: " << buffer << std::endl;
   gSystem->Exec(buffer);
}

void wwwPublisher::dumpHisto(TCanvas* h,const char* outpath)
{
   if(std::string(h->GetName())=="njb" || std::string(h->GetName())=="ZbbM2D") return; // to be checked later
   std::cout << "saving " << h->GetName() << std::endl;
   char buffer[1024];
   sprintf(buffer,"%s/%s.png",outpath,h->GetName());
   h->Print(buffer);
//   sprintf(buffer,"%s/%s.eps",outpath,h->GetName());
//   h->Print(buffer);
}

void wwwPublisher::createMenuHeader(const char* path)
{
   if(menu) return;
   menu = new ofstream(Form("%s/menu.html",path));
   basepath = path;
   basepath += "/";
   char buffer[700] =
     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\"> \n"
     "<html> \n"
     "<head> \n"
     "<title>control plots: Menu</title> \n"
     "</head> \n"
     "<BODY TEXT=\"#000066\" BGCOLOR=\"#CCCCFF\"  LINK=\"#FFFF00\" VLINK=\"#FF00FF\" > \n"
     "<base target=\"content\">  \n"
     "<P> \n"
     "<TABLE WIDTH=\"100%\"> \n"
     "<TR> \n"
     "<TH ALIGN=\"center\" width=\"40%\" BGCOLOR=\"#9999FF\"><FONT \n"
     "COLOR=\"#FFFFFF\" SIZE=+1> Menu </FONT></TH> \n"
     "</TABLE> \n"
     "</p> \n"
     "<ul> \n";
   (*menu) << buffer << std::endl;
}

void wwwPublisher::addMenuItem(const char* name, const char* path)
{
   if(!menu) {
     createMenuHeader(path);
     // note: we don't actually add the first item.
     // there will be a spurious </ul> at the end but browsers can cope with that.
   } else {
     (*menu) << "<li><a href=" << (path+basepath.size()) << "/diow.html>" << name << "</a></li>" << std::endl;
     (*menu) << "<ul>" << std::endl;
   }
}

void wwwPublisher::closeMenuItem()
{
   (*menu) << "</ul>" << std::endl;
}

void wwwPublisher::addMenuFooter()
{
   (*menu) << "</ul>\n</body>\n</html>" << std::endl;
   menu->close();
   delete menu;
   menu = NULL;
}

void wwwPublisher::createFrames(const char* path)
{
   ofstream outfile (Form("%s/index.html",path));
   char buffer[700] =
     " <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\"> \n"
     "<html><head><title>control plots: zbb_louvain 's Images</title></head> \n"
     "<frameset cols=20%,80%><frame name=\"menu\" src=\"menu.html\"><frame name=\"content\" src=\"diow.html\"> \n"
     "</frameset></html> \n";
   outfile << buffer;
   outfile.close();
}

void publish(const char* inputFile, const char* outputPath) {
  // input File
  TFile* input = TFile::Open(inputFile);
  // set batch mode
  gROOT->SetBatch();  
  // do the job
  wwwPublisher publisher;
  publisher.traverseDir(input,outputPath);
  publisher.createFrames(outputPath);
  publisher.addMenuFooter();
}

