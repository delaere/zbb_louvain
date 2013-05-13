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


void MWToRoot(const char *inputFile1,const char *inputFile2, const char *inputFile3,const char *inputFile4,const char *inputFile5,const char *inputFile6,const char *inputFile7, const char *inputFile8,const char *LHCOFile,const char *Event_Info,TString outName, int EventToProcess, int tagg_zbb,int tagg_lep, int DYflag )
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
	cout<<" enter "<<" EventToProcess  "<<EventToProcess<<endl;  
 
        // init and read file
	int var;
	int card_num = 1;
	int Evt_number =EventToProcess;
	var = card_num * Evt_number;

	cout<<"First input file is "<< inputFile1<<endl;
	
	ifstream infile1(inputFile1);
	double *abscisse_1=new double[var];
	double *ordonnee_1=new double[var];
	double *error_1=new double[var];
	Int_t line_1 = 0;	

	ifstream infile2(inputFile2);
	double *abscisse_2=new double[var];
	double *ordonnee_2=new double[var];
	double *error_2=new double[var];
	Int_t line_2 = 0;
	
        ifstream infile3(inputFile3);
        double *abscisse_3=new double[var];
        double *ordonnee_3=new double[var];
        double *error_3=new double[var];
        Int_t line_3 = 0;

        ifstream infile4(inputFile4);
        double *abscisse_4=new double[var];
        double *ordonnee_4=new double[var];
        double *error_4=new double[var];
        Int_t line_4 = 0;

        ifstream infile5(inputFile5);
        double *abscisse_5=new double[var];
        double *ordonnee_5=new double[var];
        double *error_5=new double[var];
        Int_t line_5 = 0;

        ifstream infile6(inputFile6);
        double *abscisse_6=new double[var];
        double *ordonnee_6=new double[var];
        double *error_6=new double[var];
        Int_t line_6 = 0;

        cout<<"last input file is " <<inputFile7<<endl;


	// Higgs Weights
        ifstream infile7(inputFile7);
        double *abscisse_71=new double[var];double *abscisse_72=new double[var];double *abscisse_73=new double[var];double *abscisse_74=new double[var];double *abscisse_75=new double[var];
        double *ordonnee_71=new double[var];double *ordonnee_72=new double[var];double *ordonnee_73=new double[var];double *ordonnee_74=new double[var];double *ordonnee_75=new double[var];
        double *error_71=new double[var];double *error_72=new double[var];double *error_73=new double[var];double *error_74=new double[var];double *error_75=new double[var];
        Int_t line_71 = 0;Int_t line_72 = 0;Int_t line_73 = 0;Int_t line_74 = 0;Int_t line_75 = 0;

        ifstream infile8(inputFile8);
        double *abscisse_81=new double[var];double *abscisse_82=new double[var];double *abscisse_83=new double[var];double *abscisse_84=new double[var];double *abscisse_85=new double[var];
        double *ordonnee_81=new double[var];double *ordonnee_82=new double[var];double *ordonnee_83=new double[var];double *ordonnee_84=new double[var];double *ordonnee_85=new double[var];
        double *error_81=new double[var];double *error_82=new double[var];double *error_83=new double[var];double *error_84=new double[var];double *error_85=new double[var];
        Int_t line_81 = 0;Int_t line_82 = 0;Int_t line_83 = 0;Int_t line_84 = 0;Int_t line_85 = 0;

        cout<<outName<<endl;

	cout<<"after output creation"<<endl;
	double *nul=new double[var];
	TFile file(outName+".root","RECREATE");

	cout<<"after output creation"<<endl;
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

	for(Int_t line=0; line<(5*var);++line){
	  //cout<<" guiguig "<<line<<endl;
	  if(line<var){infile7 >> abscisse_71[line_71] >> ordonnee_71[line_71] >> error_71[line_71];line_71++;}
	  if(line<2*var&&line>(1*var -1)){infile7 >> abscisse_72[line_72] >> ordonnee_72[line_72] >> error_72[line_72];line_72++;}
          if(line<3*var&&line>(2*var -1)){infile7 >> abscisse_73[line_73] >> ordonnee_73[line_73] >> error_73[line_73];line_73++;}
          if(line<4*var&&line>(3*var -1)){infile7 >> abscisse_74[line_74] >> ordonnee_74[line_74] >> error_74[line_74];line_74++;}
          if(line<5*var&&line>(4*var -1)){infile7 >> abscisse_75[line_75] >> ordonnee_75[line_75] >> error_75[line_75];line_75++;}
	  //cout<<"abs "<<ordonnee_71[line]<<endl;
	}
        infile7.close();

        for(int line =0; line<(5*var); ++line){
          if(line<(var)){infile8 >> abscisse_81[line_81] >> ordonnee_81[line_81] >> error_81[line_81];line_81++;}
          if(line<2*var&&line>(1*var -1)){infile8 >> abscisse_82[line_82] >> ordonnee_82[line_82] >> error_82[line_82];line_82++;}
          if(line<3*var&&line>(2*var -1)){infile8 >> abscisse_83[line_83] >> ordonnee_83[line_83] >> error_83[line_83];line_83++;}
          if(line<4*var&&line>(3*var -1)){infile8 >> abscisse_84[line_84] >> ordonnee_84[line_84] >> error_84[line_84];line_84++;}
          if(line<5*var&&line>(4*var -1)){infile8 >> abscisse_85[line_85] >> ordonnee_85[line_85] >> error_85[line_85];line_85++;}
        }
        infile8.close();

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
	int flavor_j1,flavor_j2;
	double trijetM_125,fsrjetphi_125,Met2,fsrjetetapm_125,fsrjetpt_125,trijetMdr,fsrDR,PT_j1,PT_j2;//,phi_j1,phi_j2Eta_j1,Eta_j2;
	//Long64_t runNumber,eventNumber;
        ULong64_t runNumber,eventNumber;
        //tree->SetBranchAddress("codeDYprod",&codeDYprod);
	tree->SetBranchAddress("runNumber",&runNumber);
	tree->SetBranchAddress("eventNumber",&eventNumber);
        tree->SetBranchAddress("isZb",&isZb);
        tree->SetBranchAddress("isZc",&isZc);
	tree->SetBranchAddress("Flavor_j1",&flavor_j1);
        tree->SetBranchAddress("Flavor_j2",&flavor_j2);
        tree->SetBranchAddress("isZl",&isZl);
        tree->SetBranchAddress("btag_j1",&btag_j1);
        tree->SetBranchAddress("btag_j2",&btag_j2);
        tree->SetBranchAddress("Met",&Met2);
	tree->SetBranchAddress("Met_sig",&Met_sig);
        tree->SetBranchAddress("llM",&llM);
        tree->SetBranchAddress("bbM",&bbM);

	tree->SetBranchAddress("trijetM_125",&trijetM_125);
	tree->SetBranchAddress("fsrjetphi_125",&fsrjetphi_125);
	tree->SetBranchAddress("fsrjetetapm_125",&fsrjetetapm_125);
	tree->SetBranchAddress("fsrjetpt_125",&fsrjetpt_125);
	tree->SetBranchAddress("trijetMdr",&trijetMdr);
	tree->SetBranchAddress("fsrDR",&fsrDR);
	
	tree->SetBranchAddress("Pt_j1",&PT_j1);
	tree->SetBranchAddress("Pt_j2",&PT_j2);
	//tree->SetBranchAddress("phi_j1",&phi_j1);	
	//tree->SetBranchAddress("phi_j2",&phi_j2);	
	//tree->SetBranchAddress("Eta_j1",&Eta_j1);	
	//tree->SetBranchAddress("Eta_j2",&Eta_j2);		
		
        tree->SetBranchAddress("nJets",&nJets);
	tree->SetBranchAddress("nbr_PV",&nbr_PV);
	tree->SetBranchAddress("Pile_up",&Pile_up);
	//tree->SetBranchAddress("noPUcorrMeT_sig",&noPUcorrMeT_sig);
        //tree->SetBranchAddress("noPUcorrMeT_phi",&noPUcorrMeT_phi);
        //tree->SetBranchAddress("noPUcorrMeT",&noPUcorrMeT);


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
	double Whi0_115,Whi0_120,Whi0_125,Whi0_130,Whi0_135,Whi3_115,Whi3_120,Whi3_125,Whi3_130,Whi3_135;
	double Pt_j1,Pt_j2,Eta_j1,Eta_j2,Phi_j1,Phi_j2,E_j1,E_j2,bestHiggsCandidate,DRfsr;
	double MeTPhi, Met_signi, Met_signi_noC, MeTPhi_noC, MeT_noC,PileUp;
	int flavour,nbrPV, multiplicity,DYprod;
	double btagj1,btagj2;
	int Flavor_j1,Flavor_j2;
	int DY_flag;
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
        tree2->Branch("Flavor_j1",&Flavor_j1,"Flavor_j1/I");
        tree2->Branch("Flavor_j2",&Flavor_j2,"Flavor_j2/I");
		
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
        tree2->Branch("DY_flag",&DY_flag,"DY_flag/I");

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
	
	tree2->Branch("trijetM_125",&trijetM_125,"trijetM_125/D");
	tree2->Branch("fsrjetphi_125",&fsrjetphi_125,"fsrjetphi_125/D");
	tree2->Branch("fsrjetetapm_125",&fsrjetetapm_125,"fsrjetetapm_125/D");
	tree2->Branch("fsrjetpt_125",&fsrjetpt_125,"fsrjetpt_125/D");
	tree2->Branch("bestHiggsCandidate",&bestHiggsCandidate,"bestHiggsCandidate/D");
	tree2->Branch("DRfsr",&DRfsr,"DRfsr/D");
	tree2->Branch("fsrDR",&fsrDR,"fsrDR/D");
	tree2->Branch("trijetMdr",&trijetMdr,"tijietMdr/D");
		
        int even=0;

	int long EvtNum[EventToProcess];
	int EvtEntry[EventToProcess];
	int Evtok[EventToProcess];
	int long RunNbr[EventToProcess];

	int entrry=0;
	
	for (Int_t entry2 = 0; entry2 <allEntries; ++entry2){
	//for (Int_t entry2 = 0; entry2 <EventToProcess; ++entry2){
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
		EvtEntry[entrry]=entry2;
           	Evtok[entrry]=entrry;     
                EvtNum[entrry]=Event->Trigger;
		RunNbr[entrry]=Event->Number;
		entrry=entrry+1;
	}}}
	
	cout<<"***************** "<<entrry<<"$$$$$$$$$$$$$$$$$$$$$"<<endl;

	for(Int_t entry = 0; entry <allEntries2; ++entry){
	//for(Int_t entry = 0; entry <EventToProcess; ++entry){

	  even++;
	  cout<<"------------------------------------------------------------------------------------"<<endl;
	  //cout<<even<<" "<<entry<<endl;
	  treeReader->ReadEntry(entry);
          tree->GetEntry(entry);
	  cout<<" in tree1 file at entry: "<<entry<<" llM "<<llM<<" evt number "<<eventNumber<<endl;
	  int tmp_ent=-1;
	  int tmp_ent2=-1;
	  bool match=false; 
	  for(int jj=0;jj<EventToProcess; ++jj){
		//cout<<"is in loop 2 before If "<<EvtNum[jj]<<" "<<eventNumber<<endl;
		if(eventNumber==EvtNum[jj]){// && runNumber==RunNbr[jj]){
		cout<<EvtNum[jj]<<" "<<RunNbr[jj]<<endl;
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
  
	  //tree->GetEntry(entry);
	  double mEt=0.0;
	  TLorentzVector El;
	  TLorentzVector antiEl;
	  TLorentzVector Mu;
	  TLorentzVector antiMu;
	  TLorentzVector jets[2];

	  double dPhi_Met_Jet1;
	  double dPhi_Met_Jet2;

	  int jet_count=0;

	  cout<<"weights "<<-log10(ordonnee_1[tmp_ent])<<" evt nbr "<<eventNumber<<" evt entry "<<tmp_ent2<<" "<<tmp_ent<<endl;
	  cout<<flavor_j1<<" "<<flavor_j2<<endl;

	  while(jet = (TRootJet*) itJet.Next() ){
	    cout<<" JETS "<<jet->PT<<" "<<jet->Eta<<" "<<jet->Phi<<endl;
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
	   if(match==true){
              //cout<<"MET number: "<<met->MET<<" "<<Met2<<endl;
            }
	  }
	  while((Event = (TRootEvent*) itEvent.Next()) ){
	      if(match==true){
              //cout<<"Event number: "<<Event->Trigger<<" "<<eventNumber<<endl;
	    }}

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
	  if(match==true){// && mEt<50 ){//&&bbM>70 && bbM<155 && InvMassAll>350 && Dphi_Zbb>2.5 && Delta_bb<1.8 &&  Delta_ll<1.5 && Tstar >0.6 && Tstar <2){
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
	    
	    //cout<<" jet Pt ------------ "<<endl;
	    cout<<PT_j1<<" "<<jets[0].Pt()<<" "<<PT_j2<<" "<<jets[1].Pt()<<endl;

	    //cout<<codeDYprod<<endl;

            int flav=0;
	    if(tagg_zbb==0){flav=0.0;}
	    if(tagg_zbb==1){
	      if(isZb==1)flav=2;
	      if(isZc==1 && isZb==0)flav=1;
	      if(isZl==1 && isZc==0 && isZb==0)flav=0;
	    }          
	    cout<<ordonnee_1[tmp_ent]<<" "<<tmp_ent<<endl;
	    if(ordonnee_1[tmp_ent]>0.0){Wgg=-log10(ordonnee_1[tmp_ent]);}
            if(ordonnee_2[tmp_ent]>0.0){Wqq=-log10(ordonnee_2[tmp_ent]);}
	    if(ordonnee_3[tmp_ent]>0.0){Wtt=-log10(ordonnee_3[tmp_ent]);}
	    if(ordonnee_4[tmp_ent]>0.0){Wtwb=-log10(ordonnee_4[tmp_ent]);}
	    if(ordonnee_5[tmp_ent]>0.0){Wzz3=-log10(ordonnee_5[tmp_ent]);}
            if(ordonnee_6[tmp_ent]>0.0){Wzz0=-log10(ordonnee_6[tmp_ent]);}
            if(ordonnee_71[tmp_ent]>0.0){Whi3_115=-log10(ordonnee_71[tmp_ent]);}
            if(ordonnee_81[tmp_ent]>0.0){Whi0_115=-log10(ordonnee_81[tmp_ent]);}
            if(ordonnee_72[tmp_ent]>0.0){Whi3_120=-log10(ordonnee_72[tmp_ent]);}
            if(ordonnee_82[tmp_ent]>0.0){Whi0_120=-log10(ordonnee_82[tmp_ent]);}
            if(ordonnee_73[tmp_ent]>0.0){Whi3_125=-log10(ordonnee_73[tmp_ent]);}
            if(ordonnee_83[tmp_ent]>0.0){Whi0_125=-log10(ordonnee_83[tmp_ent]);}
            if(ordonnee_74[tmp_ent]>0.0){Whi3_130=-log10(ordonnee_74[tmp_ent]);}
            if(ordonnee_84[tmp_ent]>0.0){Whi0_130=-log10(ordonnee_84[tmp_ent]);}
            if(ordonnee_75[tmp_ent]>0.0){Whi3_135=-log10(ordonnee_75[tmp_ent]);}
            if(ordonnee_85[tmp_ent]>0.0){Whi0_135=-log10(ordonnee_85[tmp_ent]);}
	    
	    if(ordonnee_1[tmp_ent]==0.0){Wgg=-1;}
            if(ordonnee_2[tmp_ent]==0.0){Wqq=-1;}
	    if(ordonnee_3[tmp_ent]==0.0){Wtt=-1;}
	    //if(Wtt>35){Wtt=35;}
	    if(ordonnee_4[tmp_ent]==0.0){Wtwb=-1;}
	    if(ordonnee_5[tmp_ent]==0.0){Wzz3=-1;}
            if(ordonnee_6[tmp_ent]==0.0){Wzz0=-1;}
            if(ordonnee_71[tmp_ent]==0.0){Whi3_115=-1;}
            if(ordonnee_81[tmp_ent]==0.0){Whi0_115=-1;}
            if(ordonnee_72[tmp_ent]==0.0){Whi3_120=-1;}
            if(ordonnee_82[tmp_ent]==0.0){Whi0_120=-1;}
            if(ordonnee_73[tmp_ent]==0.0){Whi3_125=-1;}
            if(ordonnee_83[tmp_ent]==0.0){Whi0_125=-1;}
            if(ordonnee_74[tmp_ent]==0.0){Whi3_130=-1;}
            if(ordonnee_84[tmp_ent]==0.0){Whi0_130=-1;}
            if(ordonnee_75[tmp_ent]==0.0){Whi3_135=-1;}
            if(ordonnee_85[tmp_ent]==0.0){Whi0_135=-1;}




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
	    
	    DY_flag=-1;
	    if(DYflag>-1){DY_flag=DYflag;}
	    Flavor_j1=flavor_j1;
	    Flavor_j2=flavor_j2;
	    
	    //cout<<" testt "<<endl;
	    //cout<<flavor_j1<<" "<<flavor_j2<<endl;

	    
	    dPhiJ1Met=dPhi_Met_Jet1;
	    dPhiJ2Met=dPhi_Met_Jet2;
	    btagj1=btag_j1;
	    btagj2=btag_j2;
	    multiplicity=nJets;
	    PileUp=Pile_up;
	    nbrPV=nbr_PV;

	    DYprod=codeDYprod;
	    
	    if((trijetM_125 - 125) < (bbM-125)){bestHiggsCandidate=trijetM_125;}
	    if((trijetM_125 - 125) > (bbM-125)){bestHiggsCandidate=bbM;}

	    double dphi1=jets[0].Phi()-fsrjetphi_125;
	    if(dphi1>TMath::Pi()){
	      dphi1= (2*TMath::Pi()) - dphi1;
	    }
	    double DR1=sqrt(pow(jets[0].Eta()-fsrjetetapm_125,2)+pow(dphi1,2));
	    
	    double dphi2=jets[1].Phi()-fsrjetphi_125;
	    if(dphi2>TMath::Pi()){
	      dphi2= (2*TMath::Pi()) - dphi2;
	    }
	    double DR2=sqrt(pow(jets[1].Eta()-fsrjetetapm_125,2)+pow(dphi2,2));	    
	    
	    if(DR1<DR2){DRfsr=DR1;}
	    if(DR2<DR1){DRfsr=DR2;}
	    
	    cout<<"passssssssssssssssssssssss"<<endl;
	    
	    tree2->Fill();
	  }
	//}
	cout<<"passssssssssssssssssssssss555"<<endl;

        }
	
	cout<<"before write"<<endl;
	
	tree2->Write();
	file.Write();

	cout<<"after write"<<endl;

	//delete treeReader;
	//delete chain;

}
