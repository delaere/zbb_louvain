#include <string>
#include <iostream>
#include "TFile.h"
#include "TKey.h"
#include "TH1.h"

/*
 * That script allows to add to a file a directory with the sum of two directories.
 * It assumes that each of the source directories has the same structure.
 * If one of the source folder is missing, no corresponding folder is created in the sum directory.
 * If one of the sources is missing, no histogram is created in the sum directory.
 */

class CategoryAdder
{
  public:
    CategoryAdder():usePattern(false) {}
    ~CategoryAdder() {}
    void setChannel1(const char* channel, const char* pattern = "") {
      chan1 = channel;
      pattern1 = pattern;
      usePattern = (pattern1!=std::string("") && pattern2!=std::string(""));
    }
    void setChannel2(const char* channel, const char* pattern = "") {
      chan2 = channel;
      pattern2 = pattern;
      usePattern = (pattern1!=std::string("") && pattern2!=std::string(""));
    }
    void sumDir(TDirectory* dir1, TDirectory* dir2, TDirectory* output);
    void sumHistos(const char* name, TDirectory* dir1, TDirectory* dir2, TDirectory* output);

 private:
    std::string chan1, chan2, pattern1, pattern2;
    bool usePattern;

};

void CategoryAdder::sumHistos(const char* name, TDirectory* dir1, TDirectory* dir2, TDirectory* output)
{
   TH1 *h1=NULL;
   TH1 *h2=NULL;
   std::string name1 = std::string(name);
   std::string name2 = std::string(name);
   if(usePattern) {
     // name1 is the base, no need to change it.
     // substitute pattern1 by pattern2 in name2
     if(name2.find(pattern1)!=string::npos)
       name2.replace(name2.find(pattern1),pattern1.length(),pattern2);
   }
   dir1->GetObject(name1.c_str(),h1);
   dir2->GetObject(name2.c_str(),h2);
   if(!h1 || !h2) return;
   h1 = (TH1*) h1->Clone();
   h1->SetDirectory(output);
   h1->Add(h2);
   h2->SetDirectory(0);
   if(usePattern) {
     // then, remove pattern1 from output name
     if(name1.find(pattern1)!=string::npos)
       name1.replace(name1.find(pattern1),pattern1.length(),"");
   }
   h1->SetName(name1.c_str());
//   output->WriteObject(h1,h1->GetName());
}

void CategoryAdder::sumDir(TDirectory* dir1, TDirectory* dir2, TDirectory* output)
{
   dir1->SetWritable(false);
   dir2->SetWritable(false);
   output->SetWritable(true);
   TList* keys = dir1->GetListOfKeys();
   TIter next(keys);
   TKey *key;
   int delta = keys->GetEntries();
   TString nameB;
   while ((key = (TKey*) next())) {
     if(key->IsFolder()) {
        TDirectory* dirA;
        dir1->GetObject(key->GetName(),dirA);
        TDirectory* dirB;
        if(TString(key->GetName()).BeginsWith("stage_")) {
          nameB.Form("stage_%d",TString(key->GetName()+6).Atoi()+delta);
        } else {
          nameB.Form("%s",key->GetName());
        }
        dir2->GetObject((const char*)nameB,dirB);
	if(!dirA || !dirB) continue;
        sumDir(dirA,dirB, output->mkdir(key->GetName(),key->GetTitle()));
     } else if (key->ReadObj()->InheritsFrom("TH1")) {
        sumHistos(key->GetName(),dir1,dir2,output);
     }
   }
}

void sumChannels(const char* filename, const char* outputfile=NULL)
{
   char chan1[16] = "Muon";
   char chan2[16] = "Electron";
   char sum[16] = "Combined";
   TFile* file = NULL;
   TDirectory* sumdir = NULL;
   TFile* output = NULL;
   if(!outputfile) {
     file = TFile::Open(filename,"update");
     sumdir = file->mkdir(sum);
     if(sumdir==NULL) {
       std::cout << sum << " already exists. Exiting" << std::endl;
       return;
     }
   } else {
     file = TFile::Open(filename);
     output = TFile::Open(outputfile,"recreate");
     sumdir = output->mkdir(sum);
     if(sumdir==NULL) {
       std::cout << sum << " already exists. Exiting" << std::endl;
       return;
     }
   }
   TDirectory* chan1dir = (TDirectory*) file->Get(chan1);
   if(chan1dir==NULL || !chan1dir->IsFolder()) {
     std::cout << chan1 << " : not a directory. Exiting" << std::endl;
     return;
   }
   TDirectory* chan2dir = (TDirectory*) file->Get(chan2);
   if(chan1dir==NULL || !chan1dir->IsFolder()) {
     std::cout << chan1 << " : not a directory. Exiting" << std::endl;
     return;
   }
   CategoryAdder adder;
   adder.setChannel1(chan1,"Mu");
   adder.setChannel2(chan2,"Ele");
   adder.sumDir(chan1dir,chan2dir,sumdir);
   std::cout << "Closing input" << std::endl;
   if(file->IsWritable())  file->Write();
   file->Close();
   std::cout << "Saving output" << std::endl;
   if(outputfile && output) {
     output->Write();
     output->Close();
   } 
}

