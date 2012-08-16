/*
 *  MW_analysis.C
 *  
 *
 *  Created by Arnaud Pin on 15/04/09.
 *  Copyright 2009 __MyCompanyName__. All rights reserved.
 *
 */

#include "include.h"

float DR(float eta_1,float eta_2,float phi_1,float phi_2){
  float delta_phi=fabs(phi_2-phi_1);
  if(delta_phi>(TMath::Pi())){delta_phi=(2*(TMath::Pi()))-delta_phi;}
  float delta_eta=eta_2-eta_1;
  float delta_R=sqrt(pow(delta_eta,2)+pow(delta_phi,2));
  return delta_R;
}

Float_t Theta_Star(TLorentzVector v1, TLorentzVector v2){
  Float_t gamma = v1.E()/v1.M();
  Float_t betax = v1.Px()/(gamma*v1.M());
  Float_t betay = v1.Py()/(gamma*v1.M());
  Float_t betaz = v1.Pz()/(gamma*v1.M());
  v2.Boost(-betax,-betay,-betaz);

  Float_t Theta = v2.Angle(v1.Vect());

  return Theta;
}


void MWToRoot(const char *inputFile1,const char *inputFile2, const char *inputFile3,const char *inputFile4,const char *inputFile5,const char *inputFile6,const char *inputFile7, const char *inputFile8,const char *LHCOFile,const char *Event_Info,TString outName, int EventToProcess, int tagg_zbb,int tagg_lep )
{
  //------------------------- INPUTS NEEDED--------------------------------------------------------------------------//
  //  inputFile1     : gg weight Not normalized (output MW)
  //  inputFile2     : qq weight Not normalized (output MW)
  //  inputFile3     : tt weight Not normalized (output MW)
  //  inputFile4     : twb weight Not normalized (output MW)
  //  inputFile5     : zz weight Not normalized (output MW)                                                                                                                                                      
  //  inputFile6     : zz 0 weight Not normalized (output MW)
  //  inputFile7     : hi  weight Not normalized (output MW)      
  //  inputFile8      : hi 0 weight Not normalized (output MW)
  //  LHCOFile      : rootfiles with lhco events (output of CMS_to_LHCO (lhco file) converted in root file (use conversion code))
  //  Event_Info     : root file with more Events Info (output of CMS_to_LHCO last version)
  //  outname        : choose your outputfile name
  //  EventToProcess : number of events (has to be the same everywhere !)
  //  tagg_zbb       : Run on DY events ? Yes: 1, No: 0
  //  tagg_lep       : Choose your lepton:  Muons: 1, Electrons: 0
  
 
        // init and read file
	int var;
	int card_num = 1;
	int Evt_number =EventToProcess;
	var = card_num * Evt_number;
	
	ifstream infile1(inputFile1);
	Double_t abscisse_1[var];
	Double_t ordonnee_1[var];
	Double_t error_1[var];
	Int_t line_1 = 0;	

	ifstream infile2(inputFile2);
	Double_t abscisse_2[var];
	Double_t ordonnee_2[var];
	Double_t error_2[var];
	Int_t line_2 = 0;
	
        ifstream infile3(inputFile3);
        Double_t abscisse_3[var];
        Double_t ordonnee_3[var];
        Double_t error_3[var];
        Int_t line_3 = 0;

        ifstream infile4(inputFile4);
        Double_t abscisse_4[var];
        Double_t ordonnee_4[var];
        Double_t error_4[var];
        Int_t line_4 = 0;

        ifstream infile5(inputFile5);
        Double_t abscisse_5[var];
        Double_t ordonnee_5[var];
        Double_t error_5[var];
        Int_t line_5 = 0;

        ifstream infile6(inputFile6);
        Double_t abscisse_6[var];
        Double_t ordonnee_6[var];
        Double_t error_6[var];
        Int_t line_6 = 0;

        ifstream infile7(inputFile7);
        Double_t abscisse_7[var];
        Double_t ordonnee_7[var];
        Double_t error_7[var];
        Int_t line_7 = 0;

        ifstream infile8(inputFile8);
        Double_t abscisse_8[var];
        Double_t ordonnee_8[var];
        Double_t error_8[var];
        Int_t line_8 = 0;

	double nul[var];
	TFile file(outName+".root","RECREATE");

	//----------------------- load file 1 --------------------------------------------------------------
	while(infile1 >> abscisse_1[line_1] >> ordonnee_1[line_1] >> error_1[line_1]){
	  line_1++;
	}
	infile1.close();
	while(infile2 >> abscisse_2[line_2] >> ordonnee_2[line_2] >> error_2[line_2]){
	  line_2++;
	}
	infile2.close();		
        while(infile3 >> abscisse_3[line_3] >> ordonnee_3[line_3] >> error_3[line_3]){
	  line_3++;
        }
        infile3.close();
        while(infile4 >> abscisse_4[line_4] >> ordonnee_4[line_4] >> error_4[line_4]){
          line_4++;
        }
        infile4.close();
        while(infile5 >> abscisse_5[line_5] >> ordonnee_5[line_5] >> error_5[line_5]){
          line_5++;
        }
        infile5.close();
        while(infile6 >> abscisse_6[line_6] >> ordonnee_6[line_6] >> error_6[line_6]){
          line_6++;
        }
        infile6.close();
        while(infile7 >> abscisse_7[line_7] >> ordonnee_7[line_7] >> error_7[line_7]){
          line_7++;
	}
        infile7.close();
        while(infile8 >> abscisse_8[line_8] >> ordonnee_8[line_8] >> error_8[line_8]){
          line_8++;
        }
        infile5.close();
	//------------------------------------------------------------------------------------------------------                                              

	
	cout<<"Run over LHCO linked to the run"<<endl;

	//****************************************************************                                                                                                                                                
	//                              Run over LHCO linked to the run                                                                                                                                                   
	//****************************************************************                                                                                                                                                
        TChain *tree = new TChain("tree1");
        tree->Reset();
        tree->Add(Event_Info);

        int isZb,isZc,isZl;
	double btag_j1,btag_j2,Met_sig,noPUcorrMeT,noPUcorrMeT_phi,noPUcorrMeT_sig;
	double llM,bbM,Pile_up;
	int nbr_PV,nJets;
	Long64_t runNumber,eventNumber;

	tree->SetBranchAddress("runNumber",&runNumber);
	tree->SetBranchAddress("eventNumber",&eventNumber);
        tree->SetBranchAddress("isZb",&isZb);
        tree->SetBranchAddress("isZc",&isZc);
        tree->SetBranchAddress("isZl",&isZl);
        tree->SetBranchAddress("btag_j1",&btag_j1);
        tree->SetBranchAddress("btag_j2",&btag_j2);
        tree->SetBranchAddress("Met_sig",&Met_sig);
        tree->SetBranchAddress("llM",&llM);
        tree->SetBranchAddress("bbM",&bbM);
        tree->SetBranchAddress("nJets",&nJets);
	tree->SetBranchAddress("nbr_PV",&nbr_PV);
	tree->SetBranchAddress("Pile_up",&Pile_up);
	tree->SetBranchAddress("noPUcorrMeT_sig",&noPUcorrMeT_sig);
        tree->SetBranchAddress("noPUcorrMeT_phi",&noPUcorrMeT_phi);
        tree->SetBranchAddress("noPUcorrMeT",&noPUcorrMeT);


        TChain *chain= new TChain("LHCO");
	chain->Add(LHCOFile);
        cout<<LHCOFile<<endl;
        ExRootTreeReader *treeReader= new ExRootTreeReader(chain);
	Long64_t allEntries =treeReader->GetEntries();

        TClonesArray *branchJet = treeReader->UseBranch("Jet");
	TRootJet *jet;
	TIter itJet(branchJet);

	TClonesArray *branchMet = treeReader->UseBranch("MissingET");
	TRootMissingET *met;
	TIter itMet(branchMet);

	TClonesArray *branchMuon = treeReader->UseBranch("Muon");
        TRootMuon *Muon;
	TIter itMuon(branchMuon);

	TClonesArray *branchElectron = treeReader->UseBranch("Electron");
	TRootElectron *Electron;
	TIter itElectron(branchElectron);

        TTree *tree2 = new TTree("tree2","data");

        double Pt_elplus,Pt_elminus,Pt_Muplus,Pt_Muminus,Phi_elplus,Phi_elminus,Phi_Muplus,Phi_Muminus,Eta_elplus,Eta_elminus,Eta_Muplus,Eta_Muminus,Inv_Mass_lept,DR_jets,MeT,dPhiJ1Met,dPhiJ2Met,Inv_Mass_bb;
	double Wtt,Wgg,Wqq,Wzz0,Whi0,Wzz3,Whi3,Wtwb;
	double Pt_j1,Pt_j2,Eta_j1,Eta_j2,Phi_j1,Phi_j2,E_j1,E_j2;
	double MeTPhi, Met_signi, Met_signi_noC, MeTPhi_noC, MeT_noC,PileUp;
	int flavour,btagj1,btagj2,nbrPV, multiplicity;

	tree2->Branch("Pt_elplus",&Pt_elplus,"Pt_elplus/D");
	tree2->Branch("Pt_elminus",&Pt_elminus,"Pt_elminus/D");
	tree2->Branch("Pt_Muplus",&Pt_Muplus,"Pt_Muplus/D");
        tree2->Branch("Pt_Muminus",&Pt_Muminus,"Pt_Muminus/D");
        tree2->Branch("Phi_elplus",&Phi_elplus,"Phi_elplus/D");
        tree2->Branch("Phi_elminus",&Phi_elminus,"Phi_elminus/D");
        tree2->Branch("Phi_Muplus",&Phi_Muplus,"Phi_Muplus/D");
	tree2->Branch("Phi_Muminus",&Phi_Muminus,"Phi_Muminus/D");

        tree2->Branch("Eta_elplus",&Eta_elplus,"Eta_elplus/D");
	tree2->Branch("Eta_elminus",&Eta_elminus,"Eta_elminus/D");
        tree2->Branch("Eta_Muplus",&Eta_Muplus,"Eta_Muplus/D");
        tree2->Branch("Eta_Muminus",&Eta_Muminus,"Eta_Muminus/D");

        tree2->Branch("Eta_j1",&Eta_j1,"Eta_j1/D");
        tree2->Branch("Phi_j1",&Phi_j1,"Phi_j1/D");
        tree2->Branch("Pt_j1",&Pt_j1,"Pt_j1/D");
        tree2->Branch("E_j1",&E_j1,"E_j1/D");

        tree2->Branch("Eta_j2",&Eta_j2,"Eta_j2/D");
	tree2->Branch("Phi_j2",&Phi_j2,"Phi_j2/D");
        tree2->Branch("Pt_j2",&Pt_j2,"Pt_j2/D");
        tree2->Branch("E_j2",&E_j2,"E_j2/D");
        tree2->Branch("btagj1",&btagj1,"btagj1/I");
        tree2->Branch("btagj2",&btagj2,"btagj2/I");

        tree2->Branch("MeTPhi",&MeTPhi,"MeTPhi/D");
	tree2->Branch("Met_signi",&Met_signi,"Met_signi/D");
	tree2->Branch("MeT",&MeT,"MeT/D");

        tree2->Branch("MeTPhi_noC",&MeTPhi_noC,"MeTPhi_noC/D");
        tree2->Branch("Met_signi_noC",&Met_signi_noC,"Met_signi_noC/D");
        tree2->Branch("MeT_noC",&MeT_noC,"MeT_noC/D");

        tree2->Branch("dPhiJ1Met",&dPhiJ1Met,"dPhiJ1Met/D");
        tree2->Branch("dPhiJ2Met",&dPhiJ2Met,"dPhiJ2Met/D");

	tree2->Branch("Inv_Mass_bb",&Inv_Mass_bb,"Inv_Mass_bb/D");
        tree2->Branch("Inv_Mass_lept",&Inv_Mass_lept,"Inv_Mass_lept/D");
        tree2->Branch("DR_jets",&DR_jets,"DR_jets/D");
        tree2->Branch("flavour",&flavour,"flavour/I");

	tree2->Branch("nbrPV",&nbrPV,"nbrPV/I");
        tree2->Branch("PileUp",&PileUp,"PileUp/D");
        tree2->Branch("multiplicity",&multiplicity,"multiplicity/I");


        tree2->Branch("eventNumber",&eventNumber,"eventNumber/l");
        tree2->Branch("runNumber",&runNumber,"runNumber/l");

        tree2->Branch("Wgg",&Wgg,"Wgg/D");
	tree2->Branch("Wqq",&Wqq,"Wqq/D");
        tree2->Branch("Wtt",&Wtt,"Wtt/D");
        tree2->Branch("Wtwb",&Wtwb,"Wtwb/D");
        tree2->Branch("Wzz3",&Wzz3,"Wzz3/D");
        tree2->Branch("Wzz0",&Wzz0,"Wzz0/D");
        tree2->Branch("Whi3",&Whi3,"Whi3/D");
        tree2->Branch("Whi0",&Whi0,"Whi0/D");

        int even=0;

	//for(Int_t entry = 0; entry <allEntries; ++entry){
	for(Int_t entry = 0; entry <EventToProcess; ++entry){

	  even++;
	  //cout<<"------------------------------------------------------------------------------------"<<endl;
	  treeReader->ReadEntry(entry);
	  itJet.Reset();
	  itMuon.Reset();
	  itElectron.Reset();
	  itMet.Reset();
	  
	  tree->GetEntry(entry);
	  double mEt=0.0;
	  TLorentzVector El;
	  TLorentzVector antiEl;
	  TLorentzVector Mu;
	  TLorentzVector antiMu;
	  TLorentzVector jets[2];

	  double dPhi_Met_Jet1;
	  double dPhi_Met_Jet2;

	  int jet_count=0;

	  while(jet = (TRootJet*) itJet.Next() ){
	    //cout<<" JETS "<<jet->PT<<" "<<jet->Eta<<" "<<jet->Phi<<endl;
	    if(jet_count==0){jets[0].SetPtEtaPhiM(jet->PT,jet->Eta,jet->Phi,jet->Mass);}
	    if(jet_count==1){jets[1].SetPtEtaPhiM(jet->PT,jet->Eta,jet->Phi,jet->Mass);}
	    jet_count = jet_count+1;
	  }

	  while((Muon = (TRootMuon*) itMuon.Next()) ){
	    if(Muon->Charge <0){Mu.SetPtEtaPhiM(Muon->PT,Muon->Eta,Muon->Phi,0.105);}
	    if(Muon->Charge >0){antiMu.SetPtEtaPhiM(Muon->PT,Muon->Eta,Muon->Phi,0.105);}
	  }

	  while((Electron = (TRootElectron*) itElectron.Next()) ){
	    //cout<<Electron->PT<<" "<<Electron->Eta<<" "<<Electron->Phi<<endl;
	    if(Electron->Charge <0 ){El.SetPtEtaPhiM(Electron->PT,Electron->Eta,Electron->Phi,0.000511);}
	    if(Electron->Charge >0 ){antiEl.SetPtEtaPhiM(Electron->PT,Electron->Eta,Electron->Phi,0.000511);}
	  }

	  while((met = (TRootMissingET*) itMet.Next()) ){
	    mEt=met->MET;
	    MeTPhi=met->Phi;
	    dPhi_Met_Jet1=fabs(jets[0].Phi()-met->Phi);
	    if(dPhi_Met_Jet1>TMath::Pi()){
	      dPhi_Met_Jet1= (2*TMath::Pi()) - dPhi_Met_Jet1;
	    }
            dPhi_Met_Jet2=fabs(jets[1].Phi()-met->Phi);
	    if(dPhi_Met_Jet2>TMath::Pi()){
	      dPhi_Met_Jet2= (2*TMath::Pi()) - dPhi_Met_Jet2;
	    }


	  }
	  TLorentzVector bbSy;
	  bbSy=jets[0]+jets[1];
	  double mass_bb = bbSy.M();
	  
	  TLorentzVector DileptSyst;          
	  TLorentzVector FullSyst;

	  if(tagg_lep==0) DileptSyst= El+antiEl;
	  if(tagg_lep==1) DileptSyst= Mu+antiMu;
	  FullSyst = DileptSyst + bbSy ;
	  double InvMassLepton = DileptSyst.M();
          double InvMassAll = FullSyst.M();

	  double Delta_bb, Delta_ll, Dphi_Zbb, Tstar;
	  Delta_bb = DR(jets[0].Eta(),jets[1].Eta(),jets[0].Phi(),jets[1].Phi());
	  Delta_ll = DR(antiEl.Eta(),El.Eta(),antiEl.Phi(),El.Phi());
	  Dphi_Zbb=fabs(DileptSyst.Phi()-bbSy.Phi());
	  if(Dphi_Zbb>(TMath::Pi())){Dphi_Zbb=(2*(TMath::Pi()))-Dphi_Zbb;}

	  if(jets[0].Pt()>jets[1].Pt()){Tstar = Theta_Star(bbSy, jets[0]);}
          if(jets[1].Pt()>jets[0].Pt()){Tstar = Theta_Star(bbSy, jets[1]);}

	  //cout<<Inv_Mass_lept<<" "<<mEt<<endl;
	  // check cuts before output for NN
	  if(llM>6 && llM<206){// && mEt<50 ){//&& bbM>70 && bbM<155 && InvMassAll>350 && Dphi_Zbb>2.5 && Delta_bb<1.8 &&  Delta_ll<1.5 && Tstar >0.6 && Tstar <2){
	    Inv_Mass_lept = llM;//InvMassLepton;
	    Inv_Mass_bb= bbM;//mass_bb;
	    E_j1=jets[0].E();
	    E_j2=jets[1].E();
	    Eta_j1=jets[0].Eta();
	    Eta_j2=jets[1].Eta();
	    Phi_j1=jets[0].Phi();
	    Phi_j2=jets[1].Phi();
	    Pt_j1=jets[0].Pt();
	    Pt_j2=jets[1].Pt();


            int flav=0;
	    if(tagg_zbb==0){flav=0.0;}
	    if(tagg_zbb==1){
	      if(isZb==1)flav=2;
	      if(isZc==1 && isZb==0)flav=1;
	      if(isZl==1 && isZc==0 && isZb==0)flav=0;
	    }          
	    
	    if(ordonnee_1[entry]>0.0){Wgg=-log10(ordonnee_1[entry]);}
            if(ordonnee_2[entry]>0.0){Wqq=-log10(ordonnee_2[entry]);}
	    if(ordonnee_3[entry]>0.0){Wtt=-log10(ordonnee_3[entry]);}
	    if(ordonnee_4[entry]>0.0){Wtwb=-log10(ordonnee_4[entry]);}
	    if(ordonnee_5[entry]>0.0){Wzz3=-log10(ordonnee_5[entry]);}
            if(ordonnee_6[entry]>0.0){Wzz0=-log10(ordonnee_6[entry]);}
            if(ordonnee_7[entry]>0.0){Whi3=-log10(ordonnee_7[entry]);}
            if(ordonnee_8[entry]>0.0){Whi0=-log10(ordonnee_8[entry]);}
	    
	    if(ordonnee_1[entry]==0.0){Wgg=-1;}
            if(ordonnee_2[entry]==0.0){Wqq=-1;}
	    if(ordonnee_3[entry]==0.0){Wtt=-1;}
	    if(ordonnee_4[entry]==0.0){Wtwb=-1;}
	    if(ordonnee_5[entry]==0.0){Wzz3=-1;}
            if(ordonnee_6[entry]==0.0){Wzz0=-1;}
            if(ordonnee_7[entry]==0.0){Whi3=-1;}
            if(ordonnee_8[entry]==0.0){Whi0=-1;}

	    double dphi=jets[0].Phi()-jets[1].Phi();
	    if(dphi>TMath::Pi()){
	      dphi= (2*TMath::Pi()) - dphi;
	    }
	    double DR=sqrt(pow(jets[0].Eta()-jets[1].Eta(),2)+pow(dphi,2));
	    DR_jets=DR;
	    flavour=flav;
	    Pt_elplus= antiEl.Pt();
	    Pt_elminus = El.Pt();
	    Pt_Muplus = antiMu.Pt();
	    Pt_Muminus = Mu.Pt();
	    Phi_elplus= antiEl.Phi();
	    Phi_elminus= El.Phi();
	    Phi_Muplus= antiMu.Phi();
	    Phi_Muminus= Mu.Phi();
	    Eta_elplus= antiEl.Eta();
	    Eta_elminus= El.Eta();
	    Eta_Muplus= antiMu.Eta();
	    Eta_Muminus= Mu.Eta();
	    Met_signi=Met_sig;
	    MeT=mEt;
	    MeT_noC=noPUcorrMeT;
	    MeTPhi_noC=noPUcorrMeT_phi;
	    Met_signi_noC=noPUcorrMeT_sig;

	    dPhiJ1Met=dPhi_Met_Jet1;
	    dPhiJ2Met=dPhi_Met_Jet2;
	    btagj1=btag_j1;
	    btagj2=btag_j2;
	    multiplicity=nJets;
	    PileUp=Pile_up;
	    nbrPV=nbr_PV;

	    tree2->Fill();
	  }

        }
	tree2->Write();
	file.Write();

	delete treeReader;
	delete chain;

}
