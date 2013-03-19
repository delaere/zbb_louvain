#! /bin/sh

#Check for correct number of arguments
if [ $# -lt 4 ]
then
    echo "missing arguments, example : source NN_June.sh sample WP channel mass"
    echo "sample is : DY, TT or ZZ"
    echo "WP is : ML, MM or MM_N"
    echo "channel is : Mu, El or comb"
    echo "mass is : 110, 115, 120, 125, 130, 135, 140, 145 or 150. !!! for the moment use only 125 !!!"
    exit
fi

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
TString DIR("/nfs/user/acaudron/Tree2_53X/");
TString f1("ME_zbb_DY_"+channel+"_MC.root")
TString f2("ME_zbb_TT_"+channel+"_MC.root")
TString f3("ME_zbb_ZZ_"+channel+"_MC.root")
TString f4;
if($4==115){f4="ME_zbb_ZH115_"+channel+"_MC.root";}
if($4==120){f4="ME_zbb_ZH120_"+channel+"_MC.root";}
if($4==125){f4="ME_zbb_ZH125_"+channel+"_MC.root";}
if($4==130){f4="ME_zbb_ZH130_"+channel+"_MC.root";}

cout<<"Directory is "<<DIR<<endl;

// Output name
TString N1,N2,N3;
if($1==1){N1="DY_";}
if($1==2){N1="TT_";}
if($1==3){N1="ZZ_";}
if($2==0){N2="ML_CSV_2012_"+channel+"";}
if($2==1){N2="MM_CSV_2012_"+channel+"";}
if($2==2){N2="MM_N_CSV_2012_"+channel+"";}
if($4==115){N3="_ZH115";}
if($4==120){N3="_ZH120";}
if($4==125){N3="_ZH125";}
if($4==130){N3="_ZH130";}
NN=N1+N2+N3;
cout<<" OUTPUT NAME : "<<NN<<endl;
cout<<" OUTPUT root : ../../NN/NN_Higgs_vs_"<<NN<<endl;

// Structure of the NN and nbr of iteration
//TString NNStruct("$3")
//TString NNStruct("5:6:4:3")
TString NNStruct("5:3");
//TString NNStruct("7:2");
int iterations=50;
cout<<iterations<<endl;

// COmpilation and submission
.L include.h
.L Read_input.h 
.L Generic_NN_higgs_test.C+
cout<<"Start Neural_net_E"<<endl;

Neural_net_E(DIR+f1,DIR+f2,DIR+f3,DIR+f4,NN,$1,$2,NNStruct,iterations)

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
if($4==115){N3="_ZH115";}
if($4==120){N3="_ZH120";}
if($4==125){N3="_ZH125";}
if($4==130){N3="_ZH130";}

TString NN=N1+N2+N3;

int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;

TString arg1("$1");
TString arg2("$2");
TString arg3("$4");
TString epochinputtxt = "epoch_"+arg1+"_"+arg2+"_"+channel+"_"+arg3+".txt";

TFile* foutput = TFile::Open("NN_Higgs_vs_"+NN+".root","UPDATE");

.L ComputeGraphFromTrainTxt.C
cout<<"ComputeGraphFromTrainTxt"<<endl;
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
<< EOF
