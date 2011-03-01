
void testCanvas(TCanvas* plot)
{
  //get the plots
  TIter next(plot->GetListOfPrimitives());
  TIter* mc = NULL;
  TH1F* data = NULL;
  TObject* obj = NULL;
  while ((obj = next())) {
    if(obj->InheritsFrom("TH1")) {
      data = (TH1F*)obj;
    }
    if(obj->InheritsFrom("THStack")) {
      mc = new TIter(((THStack*)obj)->GetHists());
    }
  }
  TH1F* mcplot = NULL;
  while ((obj = mc->Next())) {
    if(!mcplot)
      mcplot = (TH1F*)((TH1F*)obj)->Clone("mc");
    else 
      mcplot->Add((TH1F*)obj);
  }
  // now that we have everything, go on.
  testShape(data,mcplot);
}


void testShape(TH1F* h1, TH1F* h2)
{
  test1(h1,h2);
  test2(h1,h2);
  test3(h1,h2);
}

void test1(TH1F* h1, TH1F* h2)
{
  // Kolmogorov test
  std::cout << "output of the Kolmogorov test: " << h1->KolmogorovTest(h2,"") << std::endl;
  std::cout << "output of the Kolmogorov test including normalization: " << h1->KolmogorovTest(h2,"N") << std::endl;
  // ratio plot per bin
  TH1F* ratio = h1->Clone("ratio");
  ratio->Sumw2();
  ratio->Divide(h2);
  /*
  for(int i=1;i<=h1->GetNbinsX();++i) {
    std::cout << "ratio bin " << i << " = " << ratio->GetBinContent(i) << "+/-" << ratio->GetBinError(i) << std::endl;
  }
  */
  new TCanvas;
  ratio->Draw();
}

void test2(TH1F* h1, TH1F* h2)
{
  // integral plot, left to right
  TH1F* int1 = h1->Clone("int1");
  int1->SetLineColor(1);
  int1->Sumw2();
  for(int i=1;i<=int1->GetNbinsX()+1;++i) {
    int1->SetBinContent(i,int1->GetBinContent(i)+int1->GetBinContent(i-1));
    int1->SetBinError(i,sqrt(int1->GetBinError(i)*int1->GetBinError(i)+int1->GetBinError(i-1)*int1->GetBinError(i-1)));
  }
  TH1F* int2 = h2->Clone("int2");
  int2->SetLineColor(3);
  int2->Sumw2();
  for(int i=1;i<=int2->GetNbinsX()+1;++i) {
    int2->SetBinContent(i,int2->GetBinContent(i)+int2->GetBinContent(i-1));
    int2->SetBinError(i,sqrt(int2->GetBinError(i)*int2->GetBinError(i)+int2->GetBinError(i-1)*int2->GetBinError(i-1)));
  }
  TLegend* leg1 = new TLegend(0.6,0.7,0.9,0.9);
  leg1->AddEntry(int1,"Data","PE");
  leg1->AddEntry(int2,"Z+b,Z+c,Z+l and ttbar","L");
  
  TCanvas* c2 = new TCanvas;
  c2->Divide(2,1);
  c2->cd(1);
  int1->Draw();
  int2->Draw("same");
  leg1->Draw();

  c2->cd(2);
  c2->GetPad(2)->SetLogy();
  TF1* fp = new TF1("poisson","TMath::Poisson(x,[0])",0,1000);
  TH1F* proba = int1->Clone("proba");
  proba->Reset();
  for(int i=1;i<=proba->GetNbinsX();++i) {
    fp->SetParameter(0,int2->GetBinContent(i));
    proba->SetBinContent(i,fp->Integral(int1->GetBinContent(i),1000));
  }
  proba->Draw();
}

void test3(TH1F* h1, TH1F* h2)
{
  // integral plot, right to left
  TH1F* int1 = h1->Clone("int1");
  int1->SetLineColor(1);
  int1->Sumw2();
  for(int i=int1->GetNbinsX();i>=0;--i) {
    int1->SetBinContent(i,int1->GetBinContent(i)+int1->GetBinContent(i+1));
    int1->SetBinError(i,sqrt(int1->GetBinError(i)*int1->GetBinError(i)+int1->GetBinError(i+1)*int1->GetBinError(i+1)));
  }
  TH1F* int2 = h2->Clone("int2");
  int2->SetLineColor(3);
  int2->Sumw2();
  for(int i=int1->GetNbinsX();i>=0;--i) {
    int2->SetBinContent(i,int2->GetBinContent(i)+int2->GetBinContent(i+1));
    int2->SetBinError(i,sqrt(int2->GetBinError(i)*int2->GetBinError(i)+int2->GetBinError(i+1)*int2->GetBinError(i+1)));
  }

  TLegend* leg1 = new TLegend(0.6,0.7,0.9,0.9);
  leg1->AddEntry(int1,"Data","PE");
  leg1->AddEntry(int2,"Z+b,Z+c,Z+l and ttbar","L");
  
  TCanvas* c2 = new TCanvas;
  c2->Divide(2,1);
  c2->cd(1);
  int1->Draw();
  int2->Draw("same");
  leg1->Draw();
  
  c2->cd(2);
  c2->GetPad(2)->SetLogy();
  TF1* fp = new TF1("poisson","TMath::Poisson(x,[0])",0,1000);
  TH1F* proba = int1->Clone("proba");
  proba->Reset();
  proba->SetLineColor(8);
  for(int i=1;i<=proba->GetNbinsX();++i) {
    fp->SetParameter(0,int2->GetBinContent(i));
    proba->SetBinContent(i,fp->Integral(int1->GetBinContent(i),1000));
  }
  proba->Draw();
  //leg2->Draw();
}
