#include <vector>
#include <string>
#include <utility>
#include <iostream>

#include <TFile.h>

void skimPlots(TFile* f_in, TFile* f_out)
{
  std::vector<std::pair<std::string, std::string> > plots;
  // list of plots to keep
  plots.push_back(std::make_pair(std::string("figure1a"),std::string("/Combined/stage_4/jetmetAK5PF/jet1nVertHP")));
  plots.push_back(std::make_pair(std::string("figure1b"),std::string("/Combined/stage_4/jetmetAK5PF/jet1SSVHPdisc")));
  plots.push_back(std::make_pair(std::string("figure2a"),std::string("/Combined/stage_6/selection/bestzmass")));
  plots.push_back(std::make_pair(std::string("figure2b"),std::string("/Combined/stage_6/selection/bestzpt")));
  plots.push_back(std::make_pair(std::string("figure3a"),std::string("/Combined/stage_6/jetmetAK5PF/bjet1pt")));
  plots.push_back(std::make_pair(std::string("figure3b"),std::string("/Combined/stage_6/selection/dphiZbj1")));
  std::vector<std::pair<std::string, std::string> >::const_iterator plots_iterator = plots.begin();
  for(;plots_iterator<plots.end();plots_iterator++) {
    f_out->cd();
    std::cout << plots_iterator->second.c_str() << " " << f_in->Get(plots_iterator->second.c_str()) << std::endl;
    f_in->Get(plots_iterator->second.c_str())->Write(plots_iterator->first.c_str(),TObject::kOverwrite);
  }
}

void skimPlots(const char* in, const char* out)
{
  TFile* f_in = TFile::Open(in);
  TFile* f_out = TFile::Open(out,"recreate");
  skimPlots(f_in,f_out);
  f_in->Close();
  f_out->Write();
  f_out->Close();
}

