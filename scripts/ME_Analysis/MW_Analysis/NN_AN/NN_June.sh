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

if [[ -d ${CMSSW_BASE} ]]
then
    echo 'running in CMSSW'
else
    export ROOTSYS=/nfs/soft/root/root-5.34.05-sl5_amd64_gcc41
    #export ROOTSYS=/nfs/soft/root/latest_sl5
    export PATH=$ROOTSYS/bin:$PATH
    export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH
    echo 'not running in CMSSW, setup root'
fi

echo ----------- Hello $USER -----------------------
echo "bkg sample is "$1
sample=$1
echo "WP for b-tagging is "$2
WP=$2
echo "channel is "$3
channel=$3
echo "higgs mass is "$4
mass=$4

root -l -b > logroot_${sample}_${WP}_${channel}_${mass}.txt << EOF

TString sample("${sample}")
TString WP("${WP}")
TString channel("${channel}")
TString mass("${mass}")
TString DIR("/nfs/user/acaudron/Tree2_53X/");
TString fDY("ME_zbb_DY_"+channel+"_MC.root")
TString fTT("ME_zbb_TT_"+channel+"_MC.root")
TString fZZ("ME_zbb_ZZ_"+channel+"_MC.root")
TString fZH("ME_zbb_ZH"+mass+"_"+channel+"_MC.root")

cout<<"Directory is "<<DIR<<endl;

// Output name
TString NN(sample+"_"+WP+"_CSV_2012_"+channel+"_ZH"+mass);
cout<<" OUTPUT NAME : "<<NN<<endl;
cout<<" OUTPUT root : ../../NN/NN_Higgs_vs_"<<NN<<endl;

// Structure of the NN and nbr of iteration
//TString NNStruct("$3")
//TString NNStruct("5:6:4:3")
TString NNStruct("5:3");
//TString NNStruct("7:2");
int iterations=2000;
cout<<"NNStruct "<<NNStruct<<endl;
cout<<"iterations "<<iterations<<endl;

// COmpilation and submission
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/include.h
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/Read_input.h 
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/Generic_NN_higgs_test.C+
cout<<"Start Neural_net_E"<<endl;

int s=1;
if(sample=="TT") s=2;
if(sample=="ZZ") s=3;
int wp=2;
if(WP=="MM") wp=1;
if(WP=="ML") wp=0;
Neural_net_E(DIR+fDY,DIR+fTT,DIR+fZZ,DIR+fZH,NN,s,wp,NNStruct,iterations)

.q
EOF

grep Epoch logroot_${sample}_${WP}_${channel}_${mass}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' > epoch_${sample}_${WP}_${channel}_${mass}.txt

NUMOFPOINTS=$(cat epoch_${sample}_${WP}_${channel}_${mass}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b NN*${sample}*${WP}*${channel}*${mass}*.root << EOF

//This part is copy and paste from the first time we call root

int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;

TString sample("${sample}")
TString WP("${WP}")
TString channel("${channel}")
TString mass("${mass}")
TString NN(sample+"_"+WP+"_CSV_2012_"+channel+"_ZH"+mass);

TString epochinputtxt = "epoch_"+sample+"_"+WP+"_"+channel+"_"+mass+".txt";

TFile* foutput = TFile::Open("NN_Higgs_vs_"+NN+".root","UPDATE");

.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/ComputeGraphFromTrainTxt.C
cout<<"ComputeGraphFromTrainTxt"<<endl;
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
<< EOF
