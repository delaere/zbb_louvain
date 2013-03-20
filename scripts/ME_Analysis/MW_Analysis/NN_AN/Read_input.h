
class nn_vars {
  public:
  int N;
  double *gg;
  double *qq;
  double *tt;
  double *hi;
  double *hi3;
  double *zz;
  double *zz3;
  int *flavour;
  double *deta;
  double *dphi;
  double *ptZ;
  double *ptbb;
  double *met;
  double *Mll;
  double *Mbb;
  double *Metsig;
  int * multi;
  double *hzbb;
  double *htt;
  double *hzz;
  double *tagj1;
  double *tagj2;
  int *flavor_j1;
  int *flavor_j2;
  int *evt_nbr;
  nn_vars(int size) {
    N = size;
    evt_nbr = new int[0];
    tagj1 = new double[size];
    tagj2 = new double[size];
    gg = new double[size];
    qq = new double[size];
    tt = new double[size];
    hi = new double[size];
    hi3 = new double[size];
    zz = new double[size];
    zz3 = new double[size];
    flavour = new int[size];
    deta = new double[size];
    dphi = new double[size];
    ptZ = new double[size];
    ptbb = new double[size];
    met = new double[size];
    Mll = new double[size];
    Mbb = new double[size];
    hzbb = new double[size];
    htt = new double[size];
    hzz = new double[size];
    Metsig = new double[size];
    multi = new int[size];
    flavor_j1 = new int[size];
    flavor_j2 = new int[size];
    }
};


class tree_in {
 public : 
double gg_weight;
	double qq_weight;
	double tt_weight;
        double zz_weight;
        double zz3_weight;
        double hi_weight;
        double hi3_weight;
	double Mll;
	double Mbb;
	double Met;
	double metsig;
	double deta;
	double dphi;
	double ptZ,ptbb;
	int type1;
	int type2;
	double btag_prod;
	double HvsZbb;
	double HvsTT;
	double HvsZZ;
	int Multi;
};


void Input(const char *rootFile,int N1,nn_vars *var, tree_in *sim,TTree *simu, int fill,int sig1,int sig2, int cutt)
{

// input file : read ttree
//TChain *chain;
  TChain *tree = new TChain("tree2");
  tree->Reset();
  tree->Add(rootFile);

  double Eta_j1,Eta_j2,Phi_j1,Phi_j2,MeTPhi,MeT,MeTsig;
  double Pt_lepplus,Eta_lepplus,Phi_lepplus,Pt_lepminus,Eta_lepminus,Phi_lepminus;
  double Pt_lep2plus,Eta_lep2plus,Phi_lep2plus,Pt_lep2minus,Eta_lep2minus,Phi_lep2minus;
  double Ej1,Ej2,Ptj1,Ptj2;
  double btagj1,btagj2;
  double Mll;
  double Wgg,Wqq,Wtt,Wzz,Wzz3,Whi,Whi3;
  int Flavor_j1,Flavor_j2;
  int multiplicity;
  tree->SetBranchAddress("multiplicity",&multiplicity);
  tree->SetBranchAddress("Wgg",&Wgg);
  tree->SetBranchAddress("Wqq",&Wqq);
  tree->SetBranchAddress("Wtt",&Wtt);
  tree->SetBranchAddress("Wzz0",&Wzz);
  tree->SetBranchAddress("Wzz3",&Wzz3);
  tree->SetBranchAddress("Whi0_125",&Whi);
  tree->SetBranchAddress("Whi3_125",&Whi3);
  tree->SetBranchAddress("MeTPhi",&MeTPhi);
  tree->SetBranchAddress("MeT",&MeT);
  tree->SetBranchAddress("Met_signi",&MeTsig);
  tree->SetBranchAddress("Pt_elplus",&Pt_lepplus);
  tree->SetBranchAddress("Eta_elplus",&Eta_lepplus);
  tree->SetBranchAddress("Phi_elplus",&Phi_lepplus);
  tree->SetBranchAddress("Pt_elminus",&Pt_lepminus);
  tree->SetBranchAddress("Eta_elminus",&Eta_lepminus);
  tree->SetBranchAddress("Phi_elminus",&Phi_lepminus);
  tree->SetBranchAddress("Pt_Muplus",&Pt_lep2plus);
  tree->SetBranchAddress("Eta_Muplus",&Eta_lep2plus);
  tree->SetBranchAddress("Phi_Muplus",&Phi_lep2plus);
  tree->SetBranchAddress("Pt_Muminus",&Pt_lep2minus);
  tree->SetBranchAddress("Eta_Muminus",&Eta_lep2minus);
  tree->SetBranchAddress("Phi_Muminus",&Phi_lep2minus);
  tree->SetBranchAddress("Eta_j2",&Eta_j2);
  tree->SetBranchAddress("Phi_j2",&Phi_j2);
  tree->SetBranchAddress("Eta_j1",&Eta_j1);
  tree->SetBranchAddress("Phi_j1",&Phi_j1);
  tree->SetBranchAddress("E_j2",&Ej2);
  tree->SetBranchAddress("Pt_j2",&Ptj2);
  tree->SetBranchAddress("E_j1",&Ej1);
  tree->SetBranchAddress("Pt_j1",&Ptj1);
  tree->SetBranchAddress("btagj1",&btagj1);
  tree->SetBranchAddress("btagj2",&btagj2);
  tree->SetBranchAddress("Inv_Mass_lept",&Mll);
  if(sig2==1 || sig2==2){
    tree->SetBranchAddress("Flavor_j2",&Flavor_j2);
    tree->SetBranchAddress("Flavor_j1",&Flavor_j1);
    
  }
  
  int entryy=0;
  bool evt[N1];
  for (int i=0;i<N1; ++i){	
    evt[i]=false;
    tree->GetEntry(i); // read tree Zbb 
    double dphi1 = MeTPhi-Phi_j1;
    double dphi2 = MeTPhi-Phi_j2;
    if(dphi1>TMath::Pi()){dphi1= (2*TMath::Pi()) - dphi1;}
    if(dphi2>TMath::Pi()){dphi2= (2*TMath::Pi()) - dphi2;}
    if(fabs(dphi1)<fabs(dphi2)){sim->dphi=fabs(dphi1);}
    if(fabs(dphi2)<fabs(dphi1)){sim->dphi=fabs(dphi2);}
    TLorentzVector l1,l2,b1,b2;
    if(Pt_lepplus>0.0 && Pt_lepminus>0.0){l1.SetPtEtaPhiM(Pt_lepplus,Eta_lepplus,Phi_lepplus,0.000511);}
    if(Pt_lepplus>0.0 && Pt_lepminus>0.0){l2.SetPtEtaPhiM(Pt_lepminus,Eta_lepminus,Phi_lepminus,0.000511);}
    if(Pt_lep2plus>0.0 && Pt_lep2minus>0.0){l1.SetPtEtaPhiM(Pt_lep2plus,Eta_lep2plus,Phi_lep2plus,0.105);}
    if(Pt_lep2plus>0.0 && Pt_lep2minus>0.0){l2.SetPtEtaPhiM(Pt_lep2minus,Eta_lep2minus,Phi_lep2minus,0.105);}
    b1.SetPtEtaPhiE(Ptj1,Eta_j1,Phi_j1,Ej1);
    b2.SetPtEtaPhiE(Ptj2,Eta_j2,Phi_j2,Ej2);  
    
    if(cutt==2 && MeTsig<10. && btagj1>0.679 && btagj2>0.679 && (Mll>76.) && (Mll<106.)){evt[i]=true;}
    if(cutt==1 && MeTsig<10. && btagj1>0.679 && btagj2>0.679 ) {evt[i]=true;}
    if(cutt==0 && MeTsig<10.){evt[i]=true;}

    if(evt[i]==true){      
      sim->gg_weight=Wgg;
      sim->qq_weight=Wqq;
      sim->tt_weight=Wtt;
      sim->zz_weight=Wzz;
      sim->zz3_weight=Wzz3;
      sim->hi_weight=Whi;
      sim->hi3_weight=Whi3;
      if(sim->gg_weight>300.0){sim->gg_weight=666;}
      if(sim->qq_weight>300.0){sim->qq_weight=666;}
      if(sim->tt_weight>300.0){sim->tt_weight=666;}
      if(sim->zz_weight>300.0){sim->zz_weight=666;}
      if(sim->zz3_weight>300.0){sim->zz3_weight=666;}
      if(sim->hi_weight>300.0){sim->hi_weight=666;}
      if(sim->hi3_weight>300.0){sim->hi3_weight=666;}
      var->tagj1[i]=btagj1;
      var->tagj2[i]=btagj2;
      var->flavor_j1[i]=Flavor_j1;
      var->flavor_j2[i]=Flavor_j2;   
      var->gg[i]=sim->gg_weight;
      var->qq[i]=sim->qq_weight;
      var->zz[i]=sim->zz_weight;
      var->zz3[i]=sim->zz3_weight;
      var->hi[i]=sim->hi_weight;
      var->hi3[i]=sim->hi3_weight;
      var->tt[i]=sim->tt_weight;
      sim->type1=sig1;
      sim->type2=sig2;
      sim->btag_prod=btagj1*btagj2;
      sim->deta = 10./(pow((pow(((l1+l2).M()),2) - pow(91.,2)),2)+10);//fabs(Eta_j1-Eta_j2);
      var->deta[i]=10./(pow((pow(((l1+l2).M()),2) - pow(91.,2)),2)+10);//fabs(Eta_j1-Eta_j2);
      sim-> ptZ=(l1+l2).Pt();
      sim->ptbb=(b1+b2).Pt();
      //sim->Mll=(l1+l2).M();
      sim->Mll=Mll;
      sim->Mbb=(b1+b2).M();
      var->Mll[i]=sim->Mll;
      var->Mbb[i]=sim->Mbb;
      var->dphi[i]=sim->dphi;
      var->ptZ[i]=sim->ptZ;
      var->ptbb[i]=sim->ptbb;
      var->Metsig[i]=MeTsig;
      sim->metsig=MeTsig;   
      sim->Met=MeT;
      var->met[i]=sim->Met;
      if(multiplicity>2){sim->Multi=1;}
      if(multiplicity<3){sim->Multi=0;}
      var->multi[i]=sim->Multi; 
      if(fill==1 && sig2==0){simu->Fill();entryy+=1;}
      if(fill==1 && sig2==1 && abs(Flavor_j2)==5 && abs(Flavor_j1)==5){simu->Fill();entryy+=1;}     
      if(fill==1 && sig2==2 && (abs(Flavor_j2)!=5 || abs(Flavor_j1)!=5)){simu->Fill();entryy+=1;}
    }   
  }
  var->evt_nbr[0]=entryy;
  cout<<"outtt "<<entryy<<endl;
}
