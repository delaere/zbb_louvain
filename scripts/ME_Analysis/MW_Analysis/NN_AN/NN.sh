#! /bin/sh

#This is the macro to run the training against individual backgrounds

#Check for correct number of arguments
if [ $# -lt 4 ]
then
    echo "missing arguments, example : source NN_June.sh sample WP channel mass"
    echo "sample is : DY, TT or ZZ"
    echo "WP is : ML, MM or MM_N !!! for the moment only works for ML !!!"
    echo "channel is : Mu, El or comb"
    echo "mass is : 110, 115, 120, 125, 130, 135, 140, 145 or 150. !!! for the moment use only 125 !!!"
    echo "multiplicity is "multi2" for only 2 b-jets, "multiPlus2" for more than 2 b-jets"    
    echo "NN structure (optional), for example: 4:3 (4:3 is the default)"    
    echo "Number of iterations (optional), for example: 2000"
    exit
fi

export HOME=.
export ROOTSYS=/nfs/soft/root/latest_sl5
export PATH=$ROOTSYS/bin:$PATH
export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH

echo ----------- Hello $USER -----------------------
echo "bkg sample is "$1
sample=$1
echo "WP for b-tagging is "$2
WP=$2
echo "channel is "$3
channel=$3
echo "higgs mass is "$4
mass=$4
echo "jet multiplicity is "$5
multi=$5
echo "NN structure is " $6
nnstructure=$6
echo "Number of iterations is" $7
niterations=$7
echo "If you put study in the end of the command line, the name of your outputs will be with the NN structure and the number of iteration. If not, the name will be compatible for the
merging code."


root -l -b > logroot_${sample}_${WP}_${channel}_${mass}_${multi}.txt << EOF

TString sample("${sample}")
TString WP("${WP}")
TString channel("${channel}")
TString mass("${mass}")
TString multi("${multi}")
TString nnstructure("${nnstructure}")
TString niterations("${niterations}")
TString study("${study}")

TString DIR("/home/fynu/cbeluffi/scratch/ZH_2012/CMSSW_4_4_4/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/Tree2/");

TString fDY("DY_all_"+channel+".root")
TString fTT("TT_"+channel+".root")
TString fZZ("ZZ_"+channel+".root")
TString fZH("ZH"+mass+"_"+channel+".root")
cout<<"Directory is "<<DIR<<endl;

// Output name
TString NN(sample+"_"+WP+"_CSV_2011_"+channel+"_ZH"+mass+"_"+multi);
cout<<" OUTPUT NAME : "<<NN<<endl;
cout<<" OUTPUT root : ../../NN/NN_Higgs_vs_"<<NN<<endl;

// Structure of the NN and nbr of iteration

TString NNStruct("4:3");
int iterations=20;

if (nnstructure != "") {//nnstructure option was set
  NNStruct = nnstructure;
}

if (niterations != "") {//niterations option was set
  iterations = niterations.Atoi();
}


cout<<"NNStruct "<<NNStruct<<endl;
cout<<"iterations "<<iterations<<endl;

// COmpilation and submission
.L include.h
.L Generic_NN_higgs_test.C+
cout<<"Start Neural_net_E"<<endl;

int s=1;
if(sample=="TT") s=2;
if(sample=="ZZ") s=3;
int wp=0;
int multiplicity=0
if(multi=="multi2") multiplicity=0;
if(multi=="multiPlus2") multiplicity=1;

double Mass=0;
if(mass=="115") Mass=115;
if(mass=="120") Mass=120;
if(mass=="125") Mass=125;
if(mass=="130") Mass=130;
if(mass=="135") Mass=135;


//Apply ptj1, ptj2, and ptz cuts
//setPtJ1Cut(40);
//setPtJ2Cut(25);
//setPtZCut(20);
Neural_net_E(DIR+fDY,DIR+fTT,DIR+fZZ,DIR+fZH,NN,s,NNStruct,iterations, multiplicity,study)

.q
EOF

grep Epoch logroot_${sample}_${WP}_${channel}_${mass}_${multi}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' >epoch_${sample}_${WP}_${channel}_${mass}_${multi}.txt

NUMOFPOINTS=$(cat epoch_${sample}_${WP}_${channel}_${mass}_${multi}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b NN*.root << EOF

//This part is copy and paste from the first time we call root
TString nnstructure("${nnstructure}")
TString niterations("${niterations}")


int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;

TString sample("${sample}")
TString WP("${WP}")
TString channel("${channel}")
TString mass("${mass}")
TString multi("${multi}")

TString NN(sample+"_"+WP+"_CSV_2011_"+channel+"_ZH"+mass+"_"+multi);

TString epochinputtxt = "epoch_"+sample+"_"+WP+"_"+channel+"_"+mass+"_"+multi+".txt";

TFile* foutput = TFile::Open("NN_Higgs_vs_"+NN+"_"+nnstructure+"_"+niterations+".root","UPDATE");

.L ComputeGraphFromTrainTxt.C
cout<<"ComputeGraphFromTrainTxt"<<endl;
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
<< EOF
