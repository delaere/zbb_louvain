#! /bin/sh

export HOME=.
export ROOTSYS=/nfs/soft/root/latest_sl5
export PATH=$ROOTSYS/bin:$PATH
export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH

echo ----------- Hello $USER -----------------------
echo $1
echo $2
echo $3
echo $4

root -l -b > logroot_${1}_${2}_${3}_${4}.txt << EOF

gSystem->Load("libPhysics")
gSystem->Load("libEG")

// Location of the input file $3 mean ee or mm or combined
// $4 is the mass of the Higgs

TString channel("$3")
TString File("/home/fynu/arnaudp/scratch/MW_5/inputFiles/CSV_2011/tree2Files/");
TString f1("DY_"+channel+"_TREE2.root")
TString f2("TT_"+channel+"_TREE2.root")
TString f3("ZZ_"+channel+"_TREE2.root")
TString f4;
if($4==115){f4="ZH115_"+channel+"_TREE2.root";}
if($4==120){f4="ZH120_"+channel+"_TREE2.root";}
if($4==125){f4="ZH125_"+channel+"_TREE2.root";}
if($4==130){f4="ZH130_"+channel+"_TREE2.root";}



cout<<f1<<endl;

// Output name
TString N1,N2,N3;
if($1==1){N1="DY_";}
if($1==2){N1="TT_";}
if($1==3){N1="ZZ_";}
if($2==0){N2="ML_CSV_2011_"+channel+"";}
if($2==1){N2="MM_CSV_2011_"+channel+"";}
if($2==2){N2="MM_N_CSV_2011_"+channel+"";}
if($4==115){N3="ZH115_";}
if($4==120){N3="ZH120_";}
if($4==125){N3="ZH125_";}
if($4==130){N3="ZH130_";}
NN=N1+N2+N3;
cout<<" OUTPUT NAME : "<<NN<<endl;
cout<<" OUTPUT root : ../../NN/NN_Higgs_vs_"<<NN<<endl;

// Structure of the NN and nbr of iteration
//TString NNStruct("$3")
//TString NNStruct("5:6:4:3")
//TString NNStruct("5:3");
TString NNStruct("7:2");
int iterations=10000;
cout<<iterations<<endl;


// COmpilation and submission
.L /home/fynu/cbeluffi/scratch/MEM_2012/NN_AN/include.h
.L /home/fynu/cbeluffi/scratch/MEM_2012/NN_AN/Read_input_m.h 
.L /home/fynu/cbeluffi/scratch/MEM_2012/NN_AN/Generic_NN_higgs_test.C+

Neural_net_E(File+f1,File+f2,File+f3,File+f4,NN,$1,$2,NNStruct,iterations)



.q

EOF

grep Epoch logroot_${1}_${2}_${3}_${4}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' > epoch_${1}_${2}_${3}_${4}.txt

NUMOFPOINTS=$(cat epoch_${1}_${2}_${3}_${4}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b NN*.root << EOF

//This part is copy and paste from the first time we call root
TString N1,N2,N3;
TString channel("$3")
if($1==1){N1="DY_";}
if($1==2){N1="TT_";}
if($1==3){N1="ZZ_";}
if($2==0){N2="ML_CSV_2011_"+channel+"";}
if($2==1){N2="MM_CSV_2011_"+channel+"";}
if($2==2){N2="MM_N_CSV_2011_"+channel+"";}
if($4==115){N3="ZH115_";}
if($4==120){N3="ZH120_";}
if($4==125){N3="ZH125_";}
if($4==130){N3="ZH130_";}


TString NN=N1+N2+N3;

int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;


TString arg1("$1");
TString arg2("$2");
TString arg2("$3");
TString epochinputtxt = "epoch_"+arg1+"_"+arg2+"_"+channel+arg3+".txt";

TFile* foutput = TFile::Open("NN_Higgs_vs_"+NN+".root","UPDATE");

.L /home/fynu/arnaudp/scratch/MW_5/MW_Analysis/NN_AN/Template/ComputeGraphFromTrainTxt.C
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
<< EOF
