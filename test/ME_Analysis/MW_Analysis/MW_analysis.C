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


void MWToRoot(const char *inputFileWgg,const char *inputFileWqq, const char *inputFileWtt,const char *inputFileWtt0,const char *inputFileWzz3,const char *inputFileWzz0,const char *inputFileWhi3, const char *inputFileWhi0,const char *LHCOFile,const char *Event_Info,TString outName, int EventToProcess, int tagg_zbb,int tagg_lep )
{
  //------------------------- INPUTS NEEDED--------------------------------------------------------------------------//
  //  inputFileWgg     : gg weight Not normalized (output MW)
  //  inputFileWqq     : qq weight Not normalized (output MW)
  //  inputFileWtt     : tt weight Not normalized (output MW)
  //  inputFileWtt0     : tt0 weight Not normalized (output MW)
  //  inputFileWzz3     : zz3 weight Not normalized (output MW)       
  //  inputFileWzz0     : zz0 weight Not normalized (output MW)
  //  inputFileWhi3     : hi3  weight Not normalized (output MW)      
  //  inputFileWhi0      : hi0 weight Not normalized (output MW)
  //  LHCOFile      : rootfiles with lhco events (output of CMS_to_LHCO (lhco file) converted in root file (use conversion code))
  //  Event_Info     : root file with more Events Info (output of CMS_to_LHCO last version)
  //  outname        : choose your outputfile name
  //  EventToProcess : number of events (has to be the same everywhere !)
  //  tagg_zbb       : Run on DY events ? Yes: 1, No: 0
  //  tagg_lep       : Choose your lepton:  Muons: 1, Electrons: 0
  
        cout<<"------------------------------------------------------------------------------------"<<endl;
        // init and read file
	int var;
	int card_num = 1;
	int Evt_number = EventToProcess;
	var = card_num * Evt_number;
	
	ifstream infileWgg(inputFileWgg);
	Double_t abscisse_1[var];
	Double_t ordonnee_1[var];
	Double_t error_1[var];
	Int_t line_1 = 0;	

	ifstream infileWqq(inputFileWqq);
	Double_t abscisse_2[var];
	Double_t ordonnee_2[var];
	Double_t error_2[var];
	Int_t line_2 = 0;
	
        ifstream infileWtt(inputFileWtt);
        Double_t abscisse_3[var];
        Double_t ordonnee_3[var];
        Double_t error_3[var];
        Int_t line_3 = 0;

        ifstream infileWtt0(inputFileWtt0);
        Double_t abscisse_4[var];
        Double_t ordonnee_4[var];
        Double_t error_4[var];
        Int_t line_4 = 0;
	
        ifstream infileWzz3(inputFileWzz3);
        Double_t abscisse_5[var];
        Double_t ordonnee_5[var];
        Double_t error_5[var];
        Int_t line_5 = 0;

        ifstream infileWzz0(inputFileWzz0);
        Double_t abscisse_6[var];
        Double_t ordonnee_6[var];
        Double_t error_6[var];
        Int_t line_6 = 0;

	// Higgs Weights
        ifstream infileWhi3(inputFileWhi3);
        Double_t abscisse_71[var];Double_t abscisse_72[var];Double_t abscisse_73[var];Double_t abscisse_74[var];Double_t abscisse_75[var];Double_t abscisse_76[var];Double_t abscisse_77[var];Double_t abscisse_78[var];Double_t abscisse_79[var];
        Double_t ordonnee_71[var];Double_t ordonnee_72[var];Double_t ordonnee_73[var];Double_t ordonnee_74[var];Double_t ordonnee_75[var];Double_t ordonnee_76[var];Double_t ordonnee_77[var];Double_t ordonnee_78[var];Double_t ordonnee_79[var];
        Double_t error_71[var];Double_t error_72[var];Double_t error_73[var];Double_t error_74[var];Double_t error_75[var];Double_t error_76[var];Double_t error_77[var];Double_t error_78[var];Double_t error_79[var];
        Int_t line_71 = 0;Int_t line_72 = 0;Int_t line_73 = 0;Int_t line_74 = 0;Int_t line_75 = 0;Int_t line_76 = 0;Int_t line_77 = 0;Int_t line_78 = 0;Int_t line_79 = 0;

        ifstream infileWhi0(inputFileWhi0);
        Double_t abscisse_81[var];Double_t abscisse_82[var];Double_t abscisse_83[var];Double_t abscisse_84[var];Double_t abscisse_85[var];Double_t abscisse_86[var];Double_t abscisse_87[var];Double_t abscisse_88[var];Double_t abscisse_89[var];
        Double_t ordonnee_81[var];Double_t ordonnee_82[var];Double_t ordonnee_83[var];Double_t ordonnee_84[var];Double_t ordonnee_85[var];Double_t ordonnee_86[var];Double_t ordonnee_87[var];Double_t ordonnee_88[var];Double_t ordonnee_89[var];
        Double_t error_81[var];Double_t error_82[var];Double_t error_83[var];Double_t error_84[var];Double_t error_85[var];Double_t error_86[var];Double_t error_87[var];Double_t error_88[var];Double_t error_89[var];
        Int_t line_81 = 0;Int_t line_82 = 0;Int_t line_83 = 0;Int_t line_84 = 0;Int_t line_85 = 0;Int_t line_86 = 0;Int_t line_87 = 0;Int_t line_88 = 0;Int_t line_89 = 0;

	double nul[var];
	TFile file(outName+".root","RECREATE");

	//----------------------- load file 1 --------------------------------------------------------------
	while(infileWgg >> abscisse_1[line_1] >> ordonnee_1[line_1] >> error_1[line_1]){
	  line_1++;
	}
	infileWgg.close();
	while(infileWqq >> abscisse_2[line_2] >> ordonnee_2[line_2] >> error_2[line_2]){
	  line_2++;
	}
	infileWqq.close();		
        while(infileWtt >> abscisse_3[line_3] >> ordonnee_3[line_3] >> error_3[line_3]){
	  line_3++;
        }
        infileWtt.close();
        while(infileWtt0 >> abscisse_4[line_4] >> ordonnee_4[line_4] >> error_4[line_4]){
          line_4++;
        }
        infileWtt0.close();
        while(infileWzz3 >> abscisse_5[line_5] >> ordonnee_5[line_5] >> error_5[line_5]){
          line_5++;
        }
        infileWzz3.close();
        while(infileWzz0 >> abscisse_6[line_6] >> ordonnee_6[line_6] >> error_6[line_6]){
          line_6++;
        }
        infileWzz0.close();

	for(Int_t line=0; line<(9*var);++line){
	  if(line<var){infileWhi3 >> abscisse_71[line_71] >> ordonnee_71[line_71] >> error_71[line_71];line_71++;}
	  if(line<2*var&&line>(1*var -1)){infileWhi3 >> abscisse_72[line_72] >> ordonnee_72[line_72] >> error_72[line_72];line_72++;}
          if(line<3*var&&line>(2*var -1)){infileWhi3 >> abscisse_73[line_73] >> ordonnee_73[line_73] >> error_73[line_73];line_73++;}
          if(line<4*var&&line>(3*var -1)){infileWhi3 >> abscisse_74[line_74] >> ordonnee_74[line_74] >> error_74[line_74];line_74++;}
          if(line<5*var&&line>(4*var -1)){infileWhi3 >> abscisse_75[line_75] >> ordonnee_75[line_75] >> error_75[line_75];line_75++;}
          if(line<6*var&&line>(5*var -1)){infileWhi3 >> abscisse_76[line_76] >> ordonnee_76[line_76] >> error_76[line_76];line_76++;}
          if(line<7*var&&line>(6*var -1)){infileWhi3 >> abscisse_77[line_77] >> ordonnee_77[line_77] >> error_77[line_77];line_77++;}
          if(line<8*var&&line>(7*var -1)){infileWhi3 >> abscisse_78[line_78] >> ordonnee_78[line_78] >> error_78[line_78];line_78++;}
          if(line<9*var&&line>(8*var -1)){infileWhi3 >> abscisse_79[line_79] >> ordonnee_79[line_79] >> error_79[line_79];line_79++;}
	}
        infileWhi3.close();

        for(int line =0; line<(9*var); ++line){
          if(line<(var)){infileWhi0 >> abscisse_81[line_81] >> ordonnee_81[line_81] >> error_81[line_81];line_81++;}
	  if(line<2*var&&line>(1*var -1)){infileWhi0 >> abscisse_82[line_82] >> ordonnee_82[line_82] >> error_82[line_82];line_82++;}
          if(line<3*var&&line>(2*var -1)){infileWhi0 >> abscisse_83[line_83] >> ordonnee_83[line_83] >> error_83[line_83];line_83++;}
          if(line<4*var&&line>(3*var -1)){infileWhi0 >> abscisse_84[line_84] >> ordonnee_84[line_84] >> error_84[line_84];line_84++;}
          if(line<5*var&&line>(4*var -1)){infileWhi0 >> abscisse_85[line_85] >> ordonnee_85[line_85] >> error_85[line_85];line_85++;}
	  if(line<6*var&&line>(5*var -1)){infileWhi0 >> abscisse_86[line_86] >> ordonnee_86[line_86] >> error_86[line_86];line_86++;}
          if(line<7*var&&line>(6*var -1)){infileWhi0 >> abscisse_87[line_87] >> ordonnee_87[line_87] >> error_87[line_87];line_87++;}
          if(line<8*var&&line>(7*var -1)){infileWhi0 >> abscisse_88[line_88] >> ordonnee_88[line_88] >> error_88[line_88];line_88++;}
          if(line<9*var&&line>(8*var -1)){infileWhi0 >> abscisse_89[line_89] >> ordonnee_89[line_89] >> error_89[line_89];line_89++;}
        }
        infileWhi0.close();

	//------------------------------------------------------------------------------------------------------                                              

		
	cout<<"Run over LHCO linked to the run"<<endl;

	//****************************************************************                                                                                                                                                
	//                              Run over LHCO linked to the run                                                                                                                                                   
	//****************************************************************                                                                                                                                                
        TChain *tree = new TChain("tree1");
        tree->Reset();
        tree->Add(Event_Info);
	Long64_t allEntries2 =tree->GetEntries();
	
        int isZb,isZc,isZl;
	double btag_j1,btag_j2,Met_sig,noPUcorrMeT,noPUcorrMeT_phi,noPUcorrMeT_sig;
	double llM,bbM,Pile_up;
	int nbr_PV,nJets,codeDYprod;
	ULong64_t runNumber,eventNumber;
	
        //tree->SetBranchAddress("codeDYprod",&codeDYprod);
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
	/*tree->SetBranchAddress("noPUcorrMeT_sig",&noPUcorrMeT_sig);
        tree->SetBranchAddress("noPUcorrMeT_phi",&noPUcorrMeT_phi);
        tree->SetBranchAddress("noPUcorrMeT",&noPUcorrMeT);
	*/

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

	TClonesArray *branchEvent = treeReader->UseBranch("Event");
	TRootEvent *Event;
        TIter itEvent(branchEvent);

        TTree *tree2 = new TTree("tree2","data");
	
        double Pt_elplus,Pt_elminus,Pt_Muplus,Pt_Muminus,Phi_elplus,Phi_elminus,Phi_Muplus,Phi_Muminus,Eta_elplus,Eta_elminus,Eta_Muplus,Eta_Muminus,Inv_Mass_lept,DR_jets,MeT,dPhiJ1Met,dPhiJ2Met,Inv_Mass_bb;
	double Wtt,Wgg,Wqq,Wzz0,Wzz3,Wtwb;
	double Whi0_110,Whi0_115,Whi0_120,Whi0_125,Whi0_130,Whi0_135,Whi0_140,Whi0_145,Whi0_150,Whi3_110,Whi3_115,Whi3_120,Whi3_125,Whi3_130,Whi3_135,Whi3_140,Whi3_145,Whi3_150;
	double Pt_j1,Pt_j2,Eta_j1,Eta_j2,Phi_j1,Phi_j2,E_j1,E_j2;
	double MeTPhi, Met_signi, Met_signi_noC, MeTPhi_noC, MeT_noC,PileUp;
	int flavour,nbrPV, multiplicity,DYprod;
	double btagj1,btagj2;
	
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
        tree2->Branch("btagj1",&btagj1,"btagj1/D");
        tree2->Branch("btagj2",&btagj2,"btagj2/D");

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

        tree2->Branch("DYprod",&DYprod,"DYprod/I");

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
        tree2->Branch("Whi3_110",&Whi3_110,"Whi3_110/D");
        tree2->Branch("Whi0_110",&Whi0_110,"Whi0_110/D");
        tree2->Branch("Whi3_115",&Whi3_115,"Whi3_115/D");
        tree2->Branch("Whi0_115",&Whi0_115,"Whi0_115/D");
        tree2->Branch("Whi3_120",&Whi3_120,"Whi3_120/D");
        tree2->Branch("Whi0_120",&Whi0_120,"Whi0_120/D");
        tree2->Branch("Whi3_125",&Whi3_125,"Whi3_125/D");
        tree2->Branch("Whi0_125",&Whi0_125,"Whi0_125/D");
        tree2->Branch("Whi3_130",&Whi3_130,"Whi3_130/D");
        tree2->Branch("Whi0_130",&Whi0_130,"Whi0_130/D");
        tree2->Branch("Whi3_135",&Whi3_135,"Whi3_135/D");
        tree2->Branch("Whi0_135",&Whi0_135,"Whi0_135/D");
        tree2->Branch("Whi3_140",&Whi3_140,"Whi3_140/D");
        tree2->Branch("Whi0_140",&Whi0_140,"Whi0_140/D");
        tree2->Branch("Whi3_145",&Whi3_145,"Whi3_145/D");
        tree2->Branch("Whi0_145",&Whi0_145,"Whi0_145/D");
        tree2->Branch("Whi3_150",&Whi3_150,"Whi3_150/D");
        tree2->Branch("Whi0_150",&Whi0_150,"Whi0_150/D");
	
        int even=0;

        int long * EvtNum = new int long [EventToProcess];
        int * EvtEntry = new int [EventToProcess];
        int * Evtok = new int [EventToProcess];
        int long * RunNbr = new int long [EventToProcess];

        int entryLHCO=0;

        for (Int_t entry2 = 0; entry2 <allEntries; ++entry2){
	  //for (Int_t entry2 = 0; entry2 <EventToProcess; ++entry2){       
	  if(entryLHCO==EventToProcess) break;                    
	  treeReader->ReadEntry(entry2);
	  itEvent.Reset();itJet.Reset();
	  while((Event = (TRootEvent*) itEvent.Next()) ){
	    int jet_count2=0;
	    while(jet = (TRootJet*) itJet.Next() ){
	      jet_count2 = jet_count2+1;
	      //cout<<jet->PT<<endl;                                                                                                                                                                     
	    }
	    if(jet_count2>1){//Event->Trigger>0){                                                                                                    
	      //cout<<" Is in the loop with 2 jets"<<Event->Trigger<<endl;                                                                                  
	      EvtEntry[entryLHCO]=entry2;
	      Evtok[entryLHCO]=entryLHCO;
	      EvtNum[entryLHCO]=Event->Trigger;
	      RunNbr[entryLHCO]=Event->Number;
	      entryLHCO=entryLHCO+1;
	    }
	  }
	}

        cout<<"***************** "<<entryLHCO<<"$$$$$$$$$$$$$$$$$$$$$"<<endl;

	//for(Int_t entry = 0; entry <allEntries; ++entry){
	for(Int_t entry = 0; entry <allEntries2; ++entry){
	  //for(Int_t entry = 0; entry <EventToProcess; ++entry){
	  
	  even++;
	  //cout<<"------------------------------------------------------------------------------------"<<endl;
	  treeReader->ReadEntry(entry);
          tree->GetEntry(entry);
          //cout<<" in tree1 file at entry: "<<entry<<" llM "<<llM<<" evt number "<<eventNumber<<endl;
          int tmp_ent=-1;
          int tmp_ent2=-1;
          bool match=false;
          for(int jj=0; jj<EventToProcess; ++jj){
	    //cout<<"is in loop 2 before If "<<EvtNum[jj]<<" "<<eventNumber<<endl;                                                                                                                     
	    if(eventNumber==EvtNum[jj]){// && runNumber==RunNbr[jj]){                                                                                                                                  
	      //cout<<EvtNum[jj]<<" "<<RunNbr[jj]<<endl;
	      tmp_ent=Evtok[jj];
	      tmp_ent2=EvtEntry[jj];
	      match=true;
	    }
          }

          //tmp_ent=entry;                                                                                                                                                                                 
          //tmp_ent2=entry;                                                                                                                                                                                
          if(match==true){
	    treeReader->ReadEntry(tmp_ent2);
	    //treeReader->ReadEntry(entry);                                                                                                                                                                  
          }

	  itJet.Reset();
	  itMuon.Reset();
	  itElectron.Reset();
	  itMet.Reset();
	  itEvent.Reset();

	  //	  tree->GetEntry(entry);
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
	  
	  while((Event = (TRootEvent*) itEvent.Next()) ){
	    if(match==true){
	      match=true;
	      //cout<<"Event number: "<<Event->Trigger<<" "<<eventNumber<<endl;
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
	  //Delta_bb = DR(jets[0].Eta(),jets[1].Eta(),jets[0].Phi(),jets[1].Phi());
	  //Delta_ll = DR(antiEl.Eta(),El.Eta(),antiEl.Phi(),El.Phi());
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
	    //Eta_j1=jets[0].Eta();
	    //Eta_j2=jets[1].Eta();
	    Phi_j1=jets[0].Phi();
	    Phi_j2=jets[1].Phi();
	    Pt_j1=jets[0].Pt();
	    Pt_j2=jets[1].Pt();
	    
	    //cout<<codeDYprod<<endl;

            int flav=0;
	    if(tagg_zbb==0){flav=0;}
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
            if(ordonnee_71[entry]>0.0){Whi3_110=-log10(ordonnee_71[entry]);}
            if(ordonnee_81[entry]>0.0){Whi0_110=-log10(ordonnee_81[entry]);}
            if(ordonnee_72[entry]>0.0){Whi3_115=-log10(ordonnee_72[entry]);}
            if(ordonnee_82[entry]>0.0){Whi0_115=-log10(ordonnee_82[entry]);}
            if(ordonnee_73[entry]>0.0){Whi3_120=-log10(ordonnee_73[entry]);}
            if(ordonnee_83[entry]>0.0){Whi0_120=-log10(ordonnee_83[entry]);}
            if(ordonnee_74[entry]>0.0){Whi3_125=-log10(ordonnee_74[entry]);}
            if(ordonnee_84[entry]>0.0){Whi0_125=-log10(ordonnee_84[entry]);}
            if(ordonnee_75[entry]>0.0){Whi3_130=-log10(ordonnee_75[entry]);}
            if(ordonnee_85[entry]>0.0){Whi0_130=-log10(ordonnee_85[entry]);}
            if(ordonnee_76[entry]>0.0){Whi3_135=-log10(ordonnee_76[entry]);}
            if(ordonnee_86[entry]>0.0){Whi0_135=-log10(ordonnee_86[entry]);}
            if(ordonnee_77[entry]>0.0){Whi3_140=-log10(ordonnee_77[entry]);}
            if(ordonnee_87[entry]>0.0){Whi0_140=-log10(ordonnee_87[entry]);}
            if(ordonnee_78[entry]>0.0){Whi3_145=-log10(ordonnee_78[entry]);}
            if(ordonnee_88[entry]>0.0){Whi0_145=-log10(ordonnee_88[entry]);}
            if(ordonnee_79[entry]>0.0){Whi3_150=-log10(ordonnee_79[entry]);}
            if(ordonnee_89[entry]>0.0){Whi0_150=-log10(ordonnee_89[entry]);}
	    
	    if(ordonnee_1[entry]==0.0){Wgg=50;}
            if(ordonnee_2[entry]==0.0){Wqq=50;}
	    if(ordonnee_3[entry]==0.0){Wtt=50;}
	    //if(Wtt>35){Wtt=35;}
	    if(ordonnee_4[entry]==0.0){Wtwb=50;}
	    if(ordonnee_5[entry]==0.0){Wzz3=50;}
            if(ordonnee_6[entry]==0.0){Wzz0=50;}
            if(ordonnee_71[entry]==0.0){Whi3_110=50;}
            if(ordonnee_81[entry]==0.0){Whi0_110=50;}
            if(ordonnee_72[entry]==0.0){Whi3_115=50;}
            if(ordonnee_82[entry]==0.0){Whi0_115=50;}
            if(ordonnee_73[entry]==0.0){Whi3_120=50;}
            if(ordonnee_83[entry]==0.0){Whi0_120=50;}
            if(ordonnee_74[entry]==0.0){Whi3_125=50;}
            if(ordonnee_84[entry]==0.0){Whi0_125=50;}
            if(ordonnee_75[entry]==0.0){Whi3_130=50;}
            if(ordonnee_85[entry]==0.0){Whi0_130=50;}
            if(ordonnee_76[entry]==0.0){Whi3_135=50;}
            if(ordonnee_86[entry]==0.0){Whi0_135=50;}
            if(ordonnee_77[entry]==0.0){Whi3_140=50;}
            if(ordonnee_87[entry]==0.0){Whi0_140=50;}
            if(ordonnee_78[entry]==0.0){Whi3_145=50;}
            if(ordonnee_88[entry]==0.0){Whi0_145=50;}
            if(ordonnee_79[entry]==0.0){Whi3_150=50;}
            if(ordonnee_89[entry]==0.0){Whi0_150=50;}

	    double dphi;//=jets[0].Phi()-jets[1].Phi();
	    if(dphi>TMath::Pi()){
	      dphi= (2*TMath::Pi()) - dphi;
	    }
	    double DR;//=sqrt(pow(jets[0].Eta()-jets[1].Eta(),2)+pow(dphi,2));
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
	    //Eta_elplus= antiEl.Eta();
	    //Eta_elminus= El.Eta();
	    //Eta_Muplus= antiMu.Eta();
	    //Eta_Muminus= Mu.Eta();
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

	    DYprod=codeDYprod;
	    
	    tree2->Fill();
	    if (entry == EventToProcess-1) break;
	  }
	  
        }
       
	tree2->Write();
	file.Write();
						       
	//delete treeReader;
	delete chain;
													
}
