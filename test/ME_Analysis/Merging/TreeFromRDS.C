{
  _file0->cd();
  TString name = "Tree_" + TString(_file0->GetName());
  TFile* fout = new TFile(name, "RECREATE");
  
  RooAbsData* rad = (RooDataSet*)_file0->Get("rds_zbb");
  TTree* tree = rad->tree();
  
  tree->Write();
}
