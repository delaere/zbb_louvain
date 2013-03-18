#! /bin/sh

export HOME=.
export ROOTSYS=/nfs/soft/root/latest_sl5
export PATH=$ROOTSYS/bin:$PATH
export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH

echo ----------- Hello $USER -----------------------
echo $1
echo $2


root -l -b > logroot_${1}_${2}.txt << EOF

gSystem->Load("libPhysics")
gSystem->Load("libEG")



TString channel("$2")
TString File("/home/fynu/arnaudp/scratch/MW_5/inputFiles/CSV_2011/tree2Files/");
TString f1("DY_"+channel+"_TREE2.root")
TString f2("TT_"+channel+"_TREE2.root")
TString f3("ZZ_"+channel+"_TREE2.root")
TString f4;
if($1==115){f4="ZH115_"+channel+"_TREE2.root";}
if($1==120){f4="ZH120_"+channel+"_TREE2.root";}
if($1==125){f4="ZH125_"+channel+"_TREE2.root";}
if($1==130){f4="ZH130_"+channel+"_TREE2.root";}



cout<<f1<<endl;

// Output name
TString NN;
if($1==115){NN="ZH115_";}
if($1==120){NN="ZH120_";}
if($1==125){NN="ZH125_";}
if($1==130){NN="ZH130_";}

cout<<" OUTPUT NAME : "<<NN<<endl;
cout<<" OUTPUT root : ../../NN/NN_Higgs_vs_Bkg_"<<NN<<endl;

// Structure of the NN and nbr of iteration
//TString NNStruct("$3")
//TString NNStruct("5:6:4:3")
//TString NNStruct("5:3");
TString NNStruct("5:2");
int iterations=2000;
cout<<iterations<<endl;


// COmpilation and submission
.L /home/fynu/cbeluffi/scratch/MEM_2012/NN_AN/include.h
.L /home/fynu/cbeluffi/scratch/MEM_2012/NN_AN/Read_input_NN_inputs_m.h 
.L /home/fynu/cbeluffi/scratch/MEM_2012/NN_AN/Generic_NN_higgs_NN_inputs_m.C+

Neural_net_E(File+f1,File+f2,File+f3,File+f4,NN,NNStruct,iterations)



.q

EOF

grep Epoch logroot_${1}_${2}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' > epoch_${1}_${2}.txt

NUMOFPOINTS=$(cat epoch_${1}_${2}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b NN*.root << EOF

//This part is copy and paste from the first time we call root

TString channel("$2")
TString NN;
if($1==115){NN="ZH115_";}
if($1==120){NN="ZH120_";}
if($1==125){NN="ZH125_";}
if($1==130){NN="ZH130_";}


int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;


TString arg1("$1");
TString arg2("$2");
TString epochinputtxt = "epoch_"+arg1+"_"+arg2+"_.txt";

TFile* foutput = TFile::Open("NN_Higgs_vs_Bkg_"+NN+".root","UPDATE");

.L /home/fynu/arnaudp/scratch/MW_5/MW_Analysis/NN_AN/Template/ComputeGraphFromTrainTxt.C
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
<< EOF
