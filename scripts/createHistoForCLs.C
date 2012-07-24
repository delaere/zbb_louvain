{

  TFile *_fileWrite = new TFile("toCLsTestMbb.root","RECREATE");
  _fileWrite.mkdir("mu");
  _fileWrite.mkdir("el");
  //_fileWrite.mkdir("combined");
  _fileWrite->Close();
  
  string stage = "Cut2"; string *EorM = new string[3]; string plot ="eventSelectiondijetM";

  EorM[0]="Combined";
  EorM[1]="EEChannel";
  EorM[2]="MuMuChannel";

  double * xsec = new double * [2*5];
  xsec[0]=0.03;
  xsec[1]=1090000;
  xsec[2]=0.0242;
  xsec[3]=1090000;
  xsec[4]=0.0189;
  xsec[5]=1100000;
  xsec[6]=0.0143;
  xsec[7]=1100000;
  xsec[8]=0.0103;
  xsec[9]=1096956;


  double lumi =5210;

  cout<<"Definition done"<<endl;
 
  for(int emu=0; emu<3; emu++){

    string EM = EorM[emu];
    cout<<"looking at channel "<<EM<<endl;

    //data
    /*    TFile *_fileEle2011A = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs1bin/");//ControlPlots_Ele2011A/Ele2011A_finalSum.root");
    TFile *_fileEle2011B = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs1bin/");//ControlPlots_Ele2011B/Ele2011B_finalSum.root");
    TFile *_fileMu2011A = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs1bin/");//ControlPlots_Mu2011A/Mu2011A_finalSum.root");
    TFile *_fileMu2011B = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs1bin/");//ControlPlots_Mu2011B/Mu2011B_finalSum.root");

    TH1F* data_obs = (TH1F*) _fileEle2011A->Get((EM+"/"+stage+"/"+plot).c_str());
    TH1F* datatmp = (TH1F*) _fileEle2011B->Get((EM+"/"+stage+"/"+plot).c_str());
    data_obs.Add(datatmp);
    datatmp = (TH1F*) _fileMu2011A->Get((EM+"/"+stage+"/"+plot).c_str());
    data_obs.Add(datatmp);
    datatmp = (TH1F*) _fileMu2011B->Get((EM+"/"+stage+"/"+plot).c_str());
    data_obs.Add(datatmp);
    */
    TFile *_fileDATA = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/histoStage17extraCutsDATA.root");
    TH1F* data_obs = (TH1F*) _fileDATA->Get((EM+"/"+stage+"/"+plot).c_str());

    TFile *_fileWrite = new TFile("toCLsTestMbb.root","UPDATE");
    if(EM=="MuMuChannel") _fileWrite->cd("mu");
    else if(EM=="EEChannel") _fileWrite->cd("el");
    //else _fileWrite->cd("combined");
    data_obs->SetName("data_obs");
    data_obs->SetTitle("data_obs");
    data_obs->Rebin(2);
    data_obs->SetBins(18,20,380);
    data_obs->Write();
    _fileWrite->Close();
    /*   _fileEle2011A->Close();
    _fileEle2011B->Close();
    _fileMu2011A->Close();
    _fileMu2011B->Close();*/
    _fileDATA->Close();
    cout<<"data done"<<endl;
    //end data

    //signal
    int n = 0;
    for(int m = 115; m<=135; m+=5){
      
      //if(m==130) {n+=2;continue;}
      ostringstream oss;
      oss << m;
      string mass = oss.str();
      cout<<"looking at signal of mass "<<mass<<endl;
      TFile *_fileHi = TFile::Open(("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/histoStage17extraCutsZH"+mass+".root").c_str());//("ControlPlots_ZH_"+mass+"/ZH"+mass+"_Fall11_finalSum.root").c_str()); 

      TH1F* signal = (TH1F*) _fileHi->Get((EM+"/"+stage+"/"+plot).c_str());
      signal->Scale(xsec[n]*lumi/xsec[n+1]);
      cout<<xsec[n]<<endl;
      cout<<n<<endl;
      TFile *_fileWrite = new TFile("toCLsTestMbb.root","UPDATE");
      if(EM=="MuMuChannel") _fileWrite->cd("mu");
      else if(EM=="EEChannel") _fileWrite->cd("el");
      //else _fileWrite->cd("combined");
      signal->SetName(("signal"+mass).c_str());
      signal->SetTitle(("signal"+mass).c_str());
      signal->Rebin(2);
      signal->SetBins(18,20,380);
      signal->Write();
      _fileWrite->Close();
      _fileHi->Close();
      n+=2;
    }

    cout<<"bkg"<<endl;
    //background
    TFile *_fileTT = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/histoStage17extraCutsTT.root");//ControlPlots_TT/TT_Fall11_finalSum.root");
    TH1F* TT = (TH1F*) _fileTT->Get((EM+"/"+stage+"/"+plot).c_str());                                                             
    TT->Scale(157.5*5210/59244088);
    TT->SetName("TT");
    TT->SetTitle("TT");
    TT->Rebin(2);
    TT->SetBins(18,20,380);

    TFile *_fileZZ = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/histoStage17extraCutsZZ.root");//ControlPlots_ZZ/ZZ_Fall11_finalSum.root");
    TH1F* ZZ = (TH1F*) _fileZZ->Get((EM+"/"+stage+"/"+plot).c_str());                                                             
    ZZ->Scale(6.206*5210/4191045);
    ZZ->SetName("ZZ");
    ZZ->SetTitle("ZZ");
    ZZ->Rebin(2);
    ZZ->SetBins(18,20,380);

    TFile *_fileZb = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/histoStage17extraCutsZb.root");//ControlPlots_ZbfromDY/Zb_Fall11_finalSum.root");
    TH1F* Zb = (TH1F*) _fileZb->Get((EM+"/"+stage+"/"+plot).c_str());                                                             
    Zb->Scale(3048.0*5210/36264432);
    Zb->SetName("Zb");
    Zb->SetTitle("Zb");
    Zb->Rebin(2);
    Zb->SetBins(18,20,380);

    TFile *_fileZc = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/histoStage17extraCutsZc.root");//ControlPlots_ZcfromDY/Zc_Fall11_finalSum.root");
    TH1F* Zc = (TH1F*) _fileZc->Get((EM+"/"+stage+"/"+plot).c_str());                                                             
    Zc->Scale(3048.0*5210/36264432);
    Zc->SetName("Zc");
    Zc->SetTitle("Zc");
    Zc->Rebin(2);
    Zc->SetBins(18,20,380);

    TFile *_fileZl = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/histoStage17extraCutsZl.root");//ControlPlots_ZlfromDY/Zl_Fall11_finalSum.root");
    TH1F* Zl = (TH1F*) _fileZl->Get((EM+"/"+stage+"/"+plot).c_str());                                                             
    Zl->Scale(3048.0*5210/36264432);
    Zl->SetName("Zl");
    Zl->SetTitle("Zl");
    Zl->Rebin(2);
    Zl->SetBins(18,20,380);
    /*
    TFile *_filetW = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/");//ControlPlots_tW/tW_Fall11_finalSum.root");
    TH1F* tW = (TH1F*) _filetW->Get((EM+"/"+stage+"/"+plot).c_str());                                                             
    tW->Scale(5.3*5210/814390);
    tW->SetName("tW");
    tW->SetTitle("tW");
    tW->Rebin(2);
    tW->SetBins(18,20,380);

    TFile *_filetbarW = TFile::Open("/home/fynu/acaudron/scratch/Pat444/CMSSW_4_4_4/src/UserCode/zbb_louvain/python/Higgs3bin/");//ControlPlots_tbarW/tbarW_Fall11_finalSum.root");
    TH1F* tbarW = (TH1F*) _filetbarW->Get((EM+"/"+stage+"/"+plot).c_str());                                                             
    tbarW->Scale(5.3*5210/809984);
    tbarW->SetName("tbarW");
    tbarW->SetTitle("tbarW");
    tbarW->Rebin(2);
    tbarW->SetBins(18,20,380);
    */
    TFile *_fileWrite = new TFile("toCLsTestMbb.root","UPDATE");
    if(EM=="MuMuChannel") _fileWrite->cd("mu");
    else if(EM=="EEChannel") _fileWrite->cd("el");
    //else _fileWrite->cd("combined");
    TT->Write();
    ZZ->Write();
    Zb->Write();
    Zc->Write();
    Zl->Write();
    //tW->Write();
    //tbarW->Write();
    _fileWrite->Close();
    _fileTT->Close();
    _fileZZ->Close();
    _fileZb->Close();
    _fileZc->Close();
    _fileZl->Close();
    //_filetW->Close();
    //_filetbarW->Close();

  }

  /*    
  TH1F* background = (TH1F*) _fileTT->Get((EorM+"/"+stage+"/"+plot).c_str());
  background->Scale(157.5*5210/59244088);
  TH1F* tmp = (TH1F*) _fileZZ->Get((EorM+"/"+stage+"/"+plot).c_str());
  tmp->Scale(6.206*5210/4191045);
  background->Add(tmp);
  tmp = (TH1F*) _fileZb->Get((EorM+"/"+stage+"/"+plot).c_str());
  tmp->Scale(3048.0*5210/36264432);
  background->Add(tmp);
  tmp = (TH1F*) _fileZc->Get((EorM+"/"+stage+"/"+plot).c_str());
  tmp->Scale(3048.0*5210/36264432);
  background->Add(tmp);
  tmp = (TH1F*) _fileZl->Get((EorM+"/"+stage+"/"+plot).c_str());
  tmp->Scale(3048.0*5210/36264432);
  background->Add(tmp);
  tmp = (TH1F*) _filetW->Get((EorM+"/"+stage+"/"+plot).c_str());
  tmp->Scale(5.3*5210/814390);
  background->Add(tmp);
  tmp = (TH1F*) _filetbarW->Get((EorM+"/"+stage+"/"+plot).c_str());
  tmp->Scale(5.3*5210/809984);
  background->Add(tmp);
  */
}
