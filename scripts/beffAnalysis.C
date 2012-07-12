/* macro to produce btag efficiency histograms.

   run as 
   root -l -q 'beffAnalysis.C("mybtagEfftree.root","../data/btagEfficiencies.root")'

   where mybtagEfftree.root comes from the python analysis script.
*/

void beffAnalysis(const char* input, const char* output) {
  // input
  TFile* inputFile = TFile::Open(input);
  TTree* btagEff = (TTree*)inputFile->Get("btagEff");

  // output
  TFile* outputFile = TFile::Open(output,"RECREATE");

  // histogram with proper binning... cloned later on 
  Double_t binning[23] = {25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,120,140,160,180,200,300,650};
  TH1F* ptSpectrum = new TH1F("PtSpectrum","PtSpectrum",22,binning);
  ptSpectrum->Sumw2();

  // produce the ratio plot for the 12 combinations of (SSVHE,SSVHP),(Barrel,Endcap),(b,c,l)

  TClonesArray algorithms("TCut",2);
  new(algorithms[0]) TCut("SSVHEM","ssvhe>1.74");
  new(algorithms[1]) TCut("SSVHPT","ssvhp>2.0");

  TClonesArray etaRegions("TCut",2);
  new(etaRegions[0]) TCut("Barrel","abs(eta)<1.4");
  new(etaRegions[1]) TCut("Endcaps","abs(eta)>1.4");

  TClonesArray flavor("TCut",3);
  new(flavor[0]) TCut("l","abs(flavor)!=4 && abs(flavor)!=5");
  new(flavor[1]) TCut("c","abs(flavor)==4");
  new(flavor[2]) TCut("b","abs(flavor)==5");

  for(int i=0; i< algorithms.GetEntries() ; ++i) {
    outputFile->mkdir(((TCut*)algorithms.At(i))->GetName());
    outputFile->cd(((TCut*)algorithms.At(i))->GetName());
    for(int j=0; j< etaRegions.GetEntries() ; ++j) {
      for(int k=0; k< flavor.GetEntries() ; ++k) {
        // histogram before tagging
        TH1F* pretag = ptSpectrum->Clone("pretag");
        btagEff->Draw("pt>>pretag",(*(TCut*)etaRegions.At(j))&&(*(TCut*)flavor.At(k)));
        // histogram after tagging
        TH1F* posttag = ptSpectrum->Clone("posttag");
        btagEff->Draw("pt>>posttag",(*(TCut*)algorithms.At(i))&&(*(TCut*)etaRegions.At(j))&&(*(TCut*)flavor.At(k)));
        // ratio
        TH1F* ratio = posttag->Clone(Form("h_eff_bTagOverGoodJet_pt%s_%s",((TCut*)flavor.At(k))->GetName(),
                                                                          ((TCut*)etaRegions.At(j))->GetName()));
        ratio->Divide(pretag);
        // cleanup
        delete pretag;
        delete posttag;
      }
    }
  }

  // cleanup
  algorithms.Delete();
  etaRegions.Delete();
  flavor.Delete();
  ptSpectrum->SetDirectory(0);
  outputFile->Write();
  outputFile->Close();
  inputFile->Close();
}

