//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Jul  4 22:50:36 2013 by ROOT version 5.32/00
// from TTree tree2/data
// found on file: /nfs/user/acaudron/Tree2_537/ME_zbb_ZZ_Mu_MC.root
//////////////////////////////////////////////////////////

#ifndef tree2_h
#define tree2_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class tree2 {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Double_t        Pt_elplus;
   Double_t        Pt_elminus;
   Double_t        Pt_Muplus;
   Double_t        Pt_Muminus;
   Double_t        Phi_elplus;
   Double_t        Phi_elminus;
   Double_t        Phi_Muplus;
   Double_t        Phi_Muminus;
   Double_t        Eta_elplus;
   Double_t        Eta_elminus;
   Double_t        Eta_Muplus;
   Double_t        Eta_Muminus;
   Double_t        Eta_j1;
   Double_t        Phi_j1;
   Double_t        Pt_j1;
   Double_t        E_j1;
   Double_t        Eta_j2;
   Double_t        Phi_j2;
   Double_t        Pt_j2;
   Double_t        E_j2;
   Double_t        btagj1;
   Double_t        btagj2;
   Double_t        MeTPhi;
   Double_t        Met_signi;
   Double_t        MeT;
   Double_t        MeTPhi_noC;
   Double_t        Met_signi_noC;
   Double_t        MeT_noC;
   Double_t        dPhiJ1Met;
   Double_t        dPhiJ2Met;
   Double_t        Inv_Mass_bb;
   Double_t        Inv_Mass_lept;
   Double_t        DR_jets;
   Int_t           flavour;
   Int_t           DYprod;
   Int_t           nbrPV;
   Double_t        PileUp;
   Int_t           multiplicity;
   ULong64_t       eventNumber;
   ULong64_t       runNumber;
   Double_t        Wgg;
   Double_t        Wqq;
   Double_t        Wtt;
   Double_t        Wtwb;
   Double_t        Wzz3;
   Double_t        Wzz0;
   Double_t        Whi3_110;
   Double_t        Whi0_110;
   Double_t        Whi3_115;
   Double_t        Whi0_115;
   Double_t        Whi3_120;
   Double_t        Whi0_120;
   Double_t        Whi3_125;
   Double_t        Whi0_125;
   Double_t        Whi3_130;
   Double_t        Whi0_130;
   Double_t        Whi3_135;
   Double_t        Whi0_135;
   Double_t        Whi3_140;
   Double_t        Whi0_140;
   Double_t        Whi3_145;
   Double_t        Whi0_145;
   Double_t        Whi3_150;
   Double_t        Whi0_150;

   // List of branches
   TBranch        *b_Pt_elplus;   //!
   TBranch        *b_Pt_elminus;   //!
   TBranch        *b_Pt_Muplus;   //!
   TBranch        *b_Pt_Muminus;   //!
   TBranch        *b_Phi_elplus;   //!
   TBranch        *b_Phi_elminus;   //!
   TBranch        *b_Phi_Muplus;   //!
   TBranch        *b_Phi_Muminus;   //!
   TBranch        *b_Eta_elplus;   //!
   TBranch        *b_Eta_elminus;   //!
   TBranch        *b_Eta_Muplus;   //!
   TBranch        *b_Eta_Muminus;   //!
   TBranch        *b_Eta_j1;   //!
   TBranch        *b_Phi_j1;   //!
   TBranch        *b_Pt_j1;   //!
   TBranch        *b_E_j1;   //!
   TBranch        *b_Eta_j2;   //!
   TBranch        *b_Phi_j2;   //!
   TBranch        *b_Pt_j2;   //!
   TBranch        *b_E_j2;   //!
   TBranch        *b_btagj1;   //!
   TBranch        *b_btagj2;   //!
   TBranch        *b_MeTPhi;   //!
   TBranch        *b_Met_signi;   //!
   TBranch        *b_MeT;   //!
   TBranch        *b_MeTPhi_noC;   //!
   TBranch        *b_Met_signi_noC;   //!
   TBranch        *b_MeT_noC;   //!
   TBranch        *b_dPhiJ1Met;   //!
   TBranch        *b_dPhiJ2Met;   //!
   TBranch        *b_Inv_Mass_bb;   //!
   TBranch        *b_Inv_Mass_lept;   //!
   TBranch        *b_DR_jets;   //!
   TBranch        *b_flavour;   //!
   TBranch        *b_DYprod;   //!
   TBranch        *b_nbrPV;   //!
   TBranch        *b_PileUp;   //!
   TBranch        *b_multiplicity;   //!
   TBranch        *b_eventNumber;   //!
   TBranch        *b_runNumber;   //!
   TBranch        *b_Wgg;   //!
   TBranch        *b_Wqq;   //!
   TBranch        *b_Wtt;   //!
   TBranch        *b_Wtwb;   //!
   TBranch        *b_Wzz3;   //!
   TBranch        *b_Wzz0;   //!
   TBranch        *b_Whi3_110;   //!
   TBranch        *b_Whi0_110;   //!
   TBranch        *b_Whi3_115;   //!
   TBranch        *b_Whi0_115;   //!
   TBranch        *b_Whi3_120;   //!
   TBranch        *b_Whi0_120;   //!
   TBranch        *b_Whi3_125;   //!
   TBranch        *b_Whi0_125;   //!
   TBranch        *b_Whi3_130;   //!
   TBranch        *b_Whi0_130;   //!
   TBranch        *b_Whi3_135;   //!
   TBranch        *b_Whi0_135;   //!
   TBranch        *b_Whi3_140;   //!
   TBranch        *b_Whi0_140;   //!
   TBranch        *b_Whi3_145;   //!
   TBranch        *b_Whi0_145;   //!
   TBranch        *b_Whi3_150;   //!
   TBranch        *b_Whi0_150;   //!

   tree2(TTree *tree=0);
   virtual ~tree2();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef tree2_cxx
tree2::tree2(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/nfs/user/acaudron/Tree2_537/ME_zbb_ZZ_Mu_MC.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/nfs/user/acaudron/Tree2_537/ME_zbb_ZZ_Mu_MC.root");
      }
      f->GetObject("tree2",tree);

   }
   Init(tree);
}

tree2::~tree2()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t tree2::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t tree2::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void tree2::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("Pt_elplus", &Pt_elplus, &b_Pt_elplus);
   fChain->SetBranchAddress("Pt_elminus", &Pt_elminus, &b_Pt_elminus);
   fChain->SetBranchAddress("Pt_Muplus", &Pt_Muplus, &b_Pt_Muplus);
   fChain->SetBranchAddress("Pt_Muminus", &Pt_Muminus, &b_Pt_Muminus);
   fChain->SetBranchAddress("Phi_elplus", &Phi_elplus, &b_Phi_elplus);
   fChain->SetBranchAddress("Phi_elminus", &Phi_elminus, &b_Phi_elminus);
   fChain->SetBranchAddress("Phi_Muplus", &Phi_Muplus, &b_Phi_Muplus);
   fChain->SetBranchAddress("Phi_Muminus", &Phi_Muminus, &b_Phi_Muminus);
   fChain->SetBranchAddress("Eta_elplus", &Eta_elplus, &b_Eta_elplus);
   fChain->SetBranchAddress("Eta_elminus", &Eta_elminus, &b_Eta_elminus);
   fChain->SetBranchAddress("Eta_Muplus", &Eta_Muplus, &b_Eta_Muplus);
   fChain->SetBranchAddress("Eta_Muminus", &Eta_Muminus, &b_Eta_Muminus);
   fChain->SetBranchAddress("Eta_j1", &Eta_j1, &b_Eta_j1);
   fChain->SetBranchAddress("Phi_j1", &Phi_j1, &b_Phi_j1);
   fChain->SetBranchAddress("Pt_j1", &Pt_j1, &b_Pt_j1);
   fChain->SetBranchAddress("E_j1", &E_j1, &b_E_j1);
   fChain->SetBranchAddress("Eta_j2", &Eta_j2, &b_Eta_j2);
   fChain->SetBranchAddress("Phi_j2", &Phi_j2, &b_Phi_j2);
   fChain->SetBranchAddress("Pt_j2", &Pt_j2, &b_Pt_j2);
   fChain->SetBranchAddress("E_j2", &E_j2, &b_E_j2);
   fChain->SetBranchAddress("btagj1", &btagj1, &b_btagj1);
   fChain->SetBranchAddress("btagj2", &btagj2, &b_btagj2);
   fChain->SetBranchAddress("MeTPhi", &MeTPhi, &b_MeTPhi);
   fChain->SetBranchAddress("Met_signi", &Met_signi, &b_Met_signi);
   fChain->SetBranchAddress("MeT", &MeT, &b_MeT);
   fChain->SetBranchAddress("MeTPhi_noC", &MeTPhi_noC, &b_MeTPhi_noC);
   fChain->SetBranchAddress("Met_signi_noC", &Met_signi_noC, &b_Met_signi_noC);
   fChain->SetBranchAddress("MeT_noC", &MeT_noC, &b_MeT_noC);
   fChain->SetBranchAddress("dPhiJ1Met", &dPhiJ1Met, &b_dPhiJ1Met);
   fChain->SetBranchAddress("dPhiJ2Met", &dPhiJ2Met, &b_dPhiJ2Met);
   fChain->SetBranchAddress("Inv_Mass_bb", &Inv_Mass_bb, &b_Inv_Mass_bb);
   fChain->SetBranchAddress("Inv_Mass_lept", &Inv_Mass_lept, &b_Inv_Mass_lept);
   fChain->SetBranchAddress("DR_jets", &DR_jets, &b_DR_jets);
   fChain->SetBranchAddress("flavour", &flavour, &b_flavour);
   fChain->SetBranchAddress("DYprod", &DYprod, &b_DYprod);
   fChain->SetBranchAddress("nbrPV", &nbrPV, &b_nbrPV);
   fChain->SetBranchAddress("PileUp", &PileUp, &b_PileUp);
   fChain->SetBranchAddress("multiplicity", &multiplicity, &b_multiplicity);
   fChain->SetBranchAddress("eventNumber", &eventNumber, &b_eventNumber);
   fChain->SetBranchAddress("runNumber", &runNumber, &b_runNumber);
   fChain->SetBranchAddress("Wgg", &Wgg, &b_Wgg);
   fChain->SetBranchAddress("Wqq", &Wqq, &b_Wqq);
   fChain->SetBranchAddress("Wtt", &Wtt, &b_Wtt);
   fChain->SetBranchAddress("Wtwb", &Wtwb, &b_Wtwb);
   fChain->SetBranchAddress("Wzz3", &Wzz3, &b_Wzz3);
   fChain->SetBranchAddress("Wzz0", &Wzz0, &b_Wzz0);
   fChain->SetBranchAddress("Whi3_110", &Whi3_110, &b_Whi3_110);
   fChain->SetBranchAddress("Whi0_110", &Whi0_110, &b_Whi0_110);
   fChain->SetBranchAddress("Whi3_115", &Whi3_115, &b_Whi3_115);
   fChain->SetBranchAddress("Whi0_115", &Whi0_115, &b_Whi0_115);
   fChain->SetBranchAddress("Whi3_120", &Whi3_120, &b_Whi3_120);
   fChain->SetBranchAddress("Whi0_120", &Whi0_120, &b_Whi0_120);
   fChain->SetBranchAddress("Whi3_125", &Whi3_125, &b_Whi3_125);
   fChain->SetBranchAddress("Whi0_125", &Whi0_125, &b_Whi0_125);
   fChain->SetBranchAddress("Whi3_130", &Whi3_130, &b_Whi3_130);
   fChain->SetBranchAddress("Whi0_130", &Whi0_130, &b_Whi0_130);
   fChain->SetBranchAddress("Whi3_135", &Whi3_135, &b_Whi3_135);
   fChain->SetBranchAddress("Whi0_135", &Whi0_135, &b_Whi0_135);
   fChain->SetBranchAddress("Whi3_140", &Whi3_140, &b_Whi3_140);
   fChain->SetBranchAddress("Whi0_140", &Whi0_140, &b_Whi0_140);
   fChain->SetBranchAddress("Whi3_145", &Whi3_145, &b_Whi3_145);
   fChain->SetBranchAddress("Whi0_145", &Whi0_145, &b_Whi0_145);
   fChain->SetBranchAddress("Whi3_150", &Whi3_150, &b_Whi3_150);
   fChain->SetBranchAddress("Whi0_150", &Whi0_150, &b_Whi0_150);
   Notify();
}

Bool_t tree2::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void tree2::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t tree2::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef tree2_cxx
