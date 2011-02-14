void DrawCanvas(TCanvas* canvas)
{
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  // retrieve the frame
  TFrame* frame = (TFrame*) canvas->FindObject("TFrame");
  canvas->Draw();
  float borderX = canvas->GetWindowWidth()-canvas->GetWw();
  float borderY = canvas->GetWindowHeight()-canvas->GetWh();
  canvas->SetCanvasSize(500,500);
  canvas->SetWindowSize(500+borderX,500+borderY);
  // add the label
  TLatex lat;
  lat.SetTextSize(0.04);
  frame = (TFrame*) canvas->FindObject("TFrame");
  bool logx = canvas->GetLogx();
  bool logy = canvas->GetLogy();
  canvas->SetLogx(false);
  canvas->SetLogy(false);
  canvas->Modified();
  canvas->Update();
  float x = frame->GetX1() + (frame->GetX2()-frame->GetX1())*0.03;
  float y = frame->GetY2() - (frame->GetY2()-frame->GetY1())*0.1;
  canvas->SetLogx(logx);
  canvas->SetLogy(logy);
  lat.DrawLatex(x,y,"#splitline{CMS Preliminary}{#sqrt{s} = 7 TeV, L = 36 pb^{-1}}");
  // polish the legend
  TLegend* legend = ((TLegend*)canvas->FindObject("TPave"));
  if(legend) {
    legend->SetFillColor(kWhite);
    legend->SetBorderSize(1);
  }
  // now it is up to you to arrange things and save
}
