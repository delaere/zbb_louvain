#! /bin/sh

#This is the macro to run the training against a combination of the backgrounds
#Some of the inputs are the NN trained against individual backgrounds


#Check for correct number of arguments
if [ $# -lt 1 ]
then
    echo "missing arguments, example : source NN_June.sh sample WP channel mass"
    echo "WP is : ML, MM or MM_N !!! for the moment only works for ML !!!"
    echo "channel is : Mu, El or comb"
    echo "mass is : 110, 115, 120, 125, 130, 135, 140, 145 or 150. !!! for the moment use only 125 !!!"
    echo "multiplicity is "multi2" for only 2 b-jets, "multiPlus2" for more than 2 b-jets"    
    exit
fi

export HOME=.
export ROOTSYS=/nfs/soft/root/latest_sl5
export PATH=$ROOTSYS/bin:$PATH
export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH

echo ----------- Hello $USER -----------------------
echo "jet multiplicity is "$1
multi=$1


root -l -b > logroot_Bkg_${multi}.txt << EOF

TString multi("${multi}")
TString channel="comb";
TString mass = "125";
TString DIR("/home/fynu/cbeluffi/scratch/MW_5/madweight/MW_Analysis/Tree2/");

TString fDY("DY_all_"+channel+".root")
TString fTT("TT_"+channel+".root")
TString fZZ("ZZ_"+channel+".root")
TString fZH("ZH125_"+channel+".root")
cout<<"Directory is "<<DIR<<endl;

// Output name
TString NN(multi);
cout<<" OUTPUT NAME : "<<NN<<endl;
cout<<" OUTPUT root : ../../NN/NN_Higgs_vs_"<<NN<<endl;

// Structure of the NN and nbr of iteration

TString NNStruct("4");
int iterations=1000;
cout<<"NNStruct "<<NNStruct<<endl;
cout<<"iterations "<<iterations<<endl;

// COmpilation and submission
.L include.h
.L Read_input_NN_inputs.h 
.L Generic_NN_higgs_NN_inputs.C+
cout<<"Start Neural_net_E"<<endl;

int multiplicity=0
if(multi=="multi2") multiplicity=0;
if(multi=="multiPlus2") multiplicity=1;


Neural_net_E(DIR+fDY,DIR+fTT,DIR+fZZ,DIR+fZH,NN,NNStruct,iterations, multiplicity)

.q
EOF

grep Epoch logroot_Bkg_${multi}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' > epoch_Bkg_${multi}.txt

NUMOFPOINTS=$(cat epoch_Bkg_${multi}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b NN*.root << EOF

//This part is copy and paste from the first time we call root

int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;

TString multi("${multi}")

TString NN(multi);

TString epochinputtxt = "epoch_Bkg_"+multi+".txt";

TFile* foutput = TFile::Open("NN_Higgs_vs_Bkg_"+NN+".root","UPDATE");

.L ComputeGraphFromTrainTxt.C
cout<<"ComputeGraphFromTrainTxt"<<endl;
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
<< EOF
