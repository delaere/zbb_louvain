#include <dirent.h>
#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
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
#include <DrawCanvas.C>

// this is a class to publish the content of ROOT files (histograms) on the web. 
// It extracts plots from the input files, uses diowGenerator to generate web pages, 
// and adds a simple menu for navigation between (t)directories.

// diowGenerator is a C++ version of the diow perl scrip version 1.6, 
// http://mips.as.arizona.edu/~hdole/diow/

class diowGenerator
{
  public:
    diowGenerator();
    ~diowGenerator() {}
    void setUsername(const char* user) { username_=user; }
    void setTitle(const char* title) { title_=title; }
    void setColors(const char* text="000066", const char* bg="CCCCFF", const char* link="FFFF00",
                   const char* vlink="FF00FF", const char* bar="9999FF") {
      textcolor_=text; bgcolor_=bg; linkcolor_=link; vlinkcolor_=vlink, barcolor_=bar; 
    }
    void setNcols(int N=6) { nCols_=N; }
    void setIconSize(uint32_t size=200) { iconsize_=size; }

    void createWebpage(const char* path = ".", const char* file = "index.html");
    void addItem(const char* filename);
    void finishWebpage();

    static void listdir(const char *path,std::vector<std::string>& files);

  private:
    std::string username_;
    std::string title_;
    std::string path_;
    std::string outhtml_;
    std::string textcolor_;
    std::string bgcolor_;
    std::string linkcolor_;
    std::string vlinkcolor_;
    std::string barcolor_;
    int nCols_;
    uint32_t iconsize_;
    int count_;
    std::ofstream* output_;
};

diowGenerator::diowGenerator() {
    username_ = "";
    title_ = "Digital Images on the Web";
    outhtml_ = "index.html";
    path_ = ".";
    textcolor_ = "000066";
    bgcolor_ = "CCCCFF";
    linkcolor_ = "FFFF00";
    vlinkcolor_ = "FF00FF";
    barcolor_ = "9999FF";
    nCols_ = 6;
    iconsize_ = 200;
    count_ = 0;
    output_ = NULL;
}

void diowGenerator::createWebpage(const char* path, const char* file) {
    path_ = path;
    outhtml_ = path + std::string("/") + std::string(file);
    output_ = new std::ofstream(outhtml_.c_str());
    (*output_) << "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">" << std::endl;
    (*output_) << "<html>\n<head>\n<title>" << title_ << ": " << username_ << " 's Images</title>" << std::endl;
    (*output_) << "</head>\n<BODY TEXT=\"" << textcolor_ 
            << "\" BGCOLOR=\"" << bgcolor_
            << "\" LINK=\"" << linkcolor_ 
            << "\" VLINK=\"" << vlinkcolor_ << "\" >" << std::endl;
    (*output_) << "<P>\n<TABLE WIDTH=\"100%\">\n <TR>\n<TH ALIGN=\"center\" width=\"40%\" BGCOLOR=\"" 
            << barcolor_ << "\"><FONT COLOR=\"#FFFFFF\" SIZE=+1>" 
            << title_ << "</FONT></TH>\n</TABLE>\n</p>" << std::endl;
    (*output_) << "<center><TABLE border=0 cellpadding=5 cellspacing=2>" << std::endl;
}

void diowGenerator::finishWebpage() {
    time_t rawtime;
    time ( &rawtime );
    (*output_) << "</TABLE>\n</center>\n<p>\n<hr width=\"100%\">\n<table border=0 cellspacing=0 cellpadding=0 width=\"100\%\">" << std::endl;
    (*output_) << "<tr><td><em>Created: " << ctime(&rawtime) << "</em></td><td align=right><em>\n<tr><td align=left><em>" << std::endl;
    (*output_) << "using the \"Digital Images On the Web\" C++ script\n</em></td></tr>\n</table>\n</body>\n</html>\n";
    output_->close();
}

void diowGenerator::listdir(const char *path,std::vector<std::string>& files) {
    // open the directory
    DIR *pdir = NULL; 
    pdir = opendir (path);
    struct dirent *pent = NULL;
    if (pdir == NULL) { 
        printf ("\nERROR! could not open the directory.");
        return;
    }
    // loop over files
    while ((pent = readdir (pdir))) {
        if (pent == NULL) {
            printf ("\nERROR! could not read the directory.");
            return;
        }
        files.push_back(std::string(pent->d_name));
    }
    // finally, let's close the directory
    closedir (pdir);
}

void diowGenerator::addItem(const char* filename) {
   // name of the icon file
   std::string smallfilename(filename);
   smallfilename.replace (smallfilename.size()-4,4,"_small.png");
   // create the icon file
   char command[1024];
   sprintf(command,"cd %s;convert -geometry x%d \'%s\' \'%s\' > /dev/null",path_.c_str(),iconsize_,filename,smallfilename.c_str());
   int returnval = system(command);
   if(returnval) std::cout << "Problem during the creation of the miniature for " << filename << std::endl;
   // insert in the HTML code the image and its icon
   std::string prefix = " ";
   std::string suffix = " ";
   if (count_==nCols_-1) { 
     prefix = " ";
     suffix = "</TR>";
     count_ = -1;
   }
   if (count_==0) {
     prefix = "<TR>";
     suffix = " ";
   }
   (*output_) << prefix << "<TD align=center> <a href=\"" << filename 
           << "\"><img src=\"" << smallfilename << "\"hspace=5 vspace=5 border=0 ALT=\"" 
           << filename << "\"></a>\n<br>" << filename << "</TD>" << suffix << std::endl;
   count_++;
}

class wwwPublisher
{
  public:
    wwwPublisher():menu(NULL) {}
    virtual ~wwwPublisher() {}
    void traverseDir(TDirectory* datadir, const char* outpath);
    void finishPage(const char* path) { createFrames(path); addMenuFooter(); }
  protected:
    virtual TCanvas* format(TCanvas* h) { return h; } 
  private:
    void dumpHisto(TCanvas* h,const char* outpath, diowGenerator* generator = NULL);
    void createMenuHeader(const char* path);
    void addMenuItem(const char* name, const char* path);
    void closeMenuItem();
    void createFrames(const char* path);
    void addMenuFooter();
    ofstream* menu;
    std::string basepath;
};

void wwwPublisher::traverseDir(TDirectory* datadir, const char* outpath)
{
   std::cout << "processing " << datadir->GetName() << std::endl;
   if(gSystem->mkdir(outpath)==-1) {
     std::cout << "Error: directory " << outpath << " already exists or could not be created." << std::endl;
     return;
   }
   diowGenerator generator;
   generator.setNcols(4);
   generator.setUsername("zbb_louvain");
   generator.setTitle("Control plots");
   generator.createWebpage(outpath,"diow.html");
   addMenuItem(datadir->GetTitle(), outpath);
   char buffer[1024];

   TList* keys = datadir->GetListOfKeys();
   TIter next(keys);
   TKey *key;
   while ((key = (TKey*) next())) {
     if(key->IsFolder()) {
        sprintf(buffer,"%s/%s",outpath,key->GetName());
        traverseDir((TDirectory*)key->ReadObj(),buffer);
     } else if (key->ReadObj()->InheritsFrom("TCanvas")) {
        dumpHisto((TCanvas*)key->ReadObj(),outpath,&generator);
     } else if (key->ReadObj()->InheritsFrom("TH1")) { 
        TCanvas* c = new TCanvas;
        c->SetName(key->GetName());
        TH1* h = (TH1*)key->ReadObj();
        h->Draw();
        dumpHisto(c,outpath,&generator);
        delete c;
     }
   }
   generator.finishWebpage();
   closeMenuItem();
}

void wwwPublisher::dumpHisto(TCanvas* h,const char* outpath, diowGenerator* generator)
{
   if(std::string(h->GetName())=="njb" || std::string(h->GetName())=="ZbbM2D") return; // to be checked later
   std::cout << "saving " << h->GetName() << std::endl;
   char buffer[1024];
   TLegend* legend = ((TLegend*)h->FindObject("TPave"));
   if(legend) {
     legend->SetFillColor(kWhite);
     legend->SetBorderSize(1);
   }
   sprintf(buffer,"%s/%s.png",outpath,h->GetName());
   format(h)->SaveAs(buffer);
   //sprintf(buffer,"%s/%s.eps",outpath,h->GetName());
   //h->SaveAs(buffer);
   if(generator) {
     sprintf(buffer,"%s.png",h->GetName());
     generator->addItem(buffer);
   }
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
     "<BODY TEXT=\"#000066\" BGCOLOR=\"#CCCCFF\"  LINK=\"#000066\" VLINK=\"#FF00FF\" > \n"
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

class wwwPublisherWithRatio: public wwwPublisher
{
  public:
    wwwPublisherWithRatio():wwwPublisher() {}
    virtual ~wwwPublisherWithRatio() {}
  protected:
    virtual TCanvas* format(TCanvas* h); 
};

TCanvas* wwwPublisherWithRatio::format(TCanvas* h)
{
  //DrawCanvas(h);
  //return DrawCanvasWithRatio(h);
  return h;
}

void publish(const char* inputFile, const char* outputPath) {
  // input File
  TFile* input = TFile::Open(inputFile);
  // set batch mode and proper style
  gROOT->SetBatch();  
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  // do the job
  wwwPublisherWithRatio publisher;
  publisher.traverseDir(input,outputPath);
  publisher.finishPage(outputPath); // here we finish everything.
  // note that we could call traverseDir more than once, with different outputPath.
  // the index is placed in the first outputPath and refers to all pages added.
}

