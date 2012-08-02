

class nn_vars {
  public:
  int N;
  double *gg;
  double *qq;
  double *tt;
  double *hi;
  double *zz;
  int *flavour;
  double *deta;
  double *dphi;
  double *ptZ;
  double *ptbb;
  double *met;
  double *Mll;
  double *Mbb;
  nn_vars(int size) {
    N = size;
    gg = new double[size];
    qq = new double[size];
    tt = new double[size];
    hi = new double[size];
    zz = new double[size];
    flavour = new int[size];
    deta = new double[size];
    dphi = new double[size];
    ptZ = new double[size];
    ptbb = new double[size];
    met = new double[size];
    Mll = new double[size];
    Mbb = new double[size];
  }
};


class tree_in {
 public : 
double gg_weight;
	double qq_weight;
	double tt_weight;
        double zz_weight;
        double hi_weight;
	double Mll;
	double Mbb;
	double Met;
	double deta;
	double dphi;
	double ptZ,ptbb;
	int type;
};


void Input(const char *rootFile,int N1,nn_vars *var, tree_in *sim,TTree *simu, int fill, int sig)
{

// input file : read ttree
TChain *chain;
TChain *tree = new TChain("tree2");
tree->Reset();
tree->Add(rootFile);

double Eta_j1,Eta_j2,Phi_j1,Phi_j2,MeTPhi,MeT;
double Pt_lepplus,Eta_lepplus,Phi_lepplus,Pt_lepminus,Eta_lepminus,Phi_lepminus;
double Pt_lep2plus,Eta_lep2plus,Phi_lep2plus,Pt_lep2minus,Eta_lep2minus,Phi_lep2minus;
double Ej1,Ej2,Ptj1,Ptj2;
double Wgg,Wqq,Wtt,Wzz,Whi;
 tree->SetBranchAddress("Wgg",&Wgg);
 tree->SetBranchAddress("Wqq",&Wqq);
 tree->SetBranchAddress("Wtt",&Wtt);
 tree->SetBranchAddress("Wzz0",&Wzz);
 tree->SetBranchAddress("Whi3",&Whi);
 tree->SetBranchAddress("MeTPhi",&MeTPhi);
 tree->SetBranchAddress("MeT",&MeT);
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



 for (int i=0;i<N1; ++i){	
   tree->GetEntry(i); // read tree Zbb 
   sim->gg_weight=Wgg;
   sim->qq_weight=Wqq;
   //if(sig==0){sim->gg_weight=Wgg;}
   //if(sig==0){sim->qq_weight=Wqq;}
   //if(sig==1){sim->qq_weight=Wgg;}
   //if(sig==1){sim->gg_weight=Wqq;}
   sim->tt_weight=Wtt;
   sim->zz_weight=Wzz;
   sim->hi_weight=Whi;
   if(sim->gg_weight>300.0){sim->gg_weight=666;}
   if(sim->qq_weight>300.0){sim->qq_weight=666;}
   if(sim->tt_weight>300.0){sim->tt_weight=666;}
   if(sim->zz_weight>300.0){sim->zz_weight=666;}
   if(sim->hi_weight>300.0){sim->hi_weight=666;}
   var->gg[i]=sim->gg_weight;
   var->qq[i]=sim->qq_weight;
   var->zz[i]=sim->zz_weight;
   var->hi[i]=sim->hi_weight;
   var->tt[i]=sim->tt_weight;
   sim->type=sig;
   sim->deta = fabs(Eta_j1-Eta_j2);
   var->deta[i]=fabs(Eta_j1-Eta_j2);
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
   sim-> ptZ=(l1+l2).Pt();
   sim->ptbb=(b1+b2).Pt();
   sim->Mll=(l1+l2).M();
   sim->Mbb=(b1+b2).M();
   var->Mll[i]=sim->Mll;
   var->Mbb[i]=sim->Mbb;
   var->dphi[i]=sim->dphi;
   var->ptZ[i]=sim->ptZ;
   var->ptbb[i]=sim->ptbb;
   sim->Met=MeT;
   var->met[i]=sim->Met;
   if(fill==1){simu->Fill();}
   //if(ptbb >100. && ptZ>100.){simu->Fill();}  
   //if(Met <50. && Mll>76. && Mll<106.){simu->Fill();}  
   
 }

 
}
