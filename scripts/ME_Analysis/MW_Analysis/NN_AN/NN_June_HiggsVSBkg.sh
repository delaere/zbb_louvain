#! /bin/sh

#Check for correct number of arguments
if [ $# -lt 2 ]
then
    echo "missing arguments, example : source NN_June_HiggsVSBkg.sh channel"
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
echo "channel is "$1
channel=$1
echo "higgs mass is "$2
mass=$2

root -l -b > logroot_${mass}_${channel}.txt << EOF

TString channel("${channel}")
TString mass("${mass}")
TString DIR("/nfs/user/acaudron/Tree2_53X/");
TString fDY("ME_zbb_DY_"+channel+"_MC.root")
TString fTT("ME_zbb_TT_"+channel+"_MC.root")
TString fZZ("ME_zbb_ZZ_"+channel+"_MC.root")
TString fZH("ME_zbb_ZH"+mass+"_"+channel+"_MC.root")

cout<<"Directory is "<<DIR<<endl;

// Output name
TString NN("ZH"+mass+"_"+channel);
cout<<" OUTPUT NAME : "<<NN<<endl;
cout<<" OUTPUT root : ../../NN/NN_Higgs_vs_Bkg_"<<NN<<endl;

// Structure of the NN and nbr of iteration
//TString NNStruct("$3")
//TString NNStruct("5:6:4:3")
TString NNStruct("5:3");
//TString NNStruct("5:2");
int iterations=100;
cout<<iterations<<endl;


// COmpilation and submission
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/include.h
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/Read_input_NN_inputs.h 
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/Generic_NN_higgs_NN_inputs.C+

Neural_net_E(DIR+fDY,DIR+fTT,DIR+fZZ,DIR+fZH,NN,NNStruct,iterations)

.q

EOF

grep Epoch logroot_${mass}_${channel}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' > epoch_${mass}_${channel}.txt

NUMOFPOINTS=$(cat epoch_${mass}_${channel}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b NN*${mass}*${channel}*.root << EOF

//This part is copy and paste from the first time we call root

TString channel("${channel}")
TString mass("${mass}")
TString NN("ZH"+mass+"_"+channel);

int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;

TString epochinputtxt = "epoch_"+mass+"_"+channel+".txt";

TFile* foutput = TFile::Open("NN_Higgs_vs_Bkg_"+NN+".root","UPDATE");

.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/ComputeGraphFromTrainTxt.C
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
<< EOF
