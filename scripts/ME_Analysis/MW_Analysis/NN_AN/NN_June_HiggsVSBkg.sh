#! /bin/sh
HOME=~acaudron/
cd /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN
source /nfs/soft/cms/cmsset_default.sh; export SCRAM_ARCH=slc5_amd64_gcc462 ; source /nfs/soft/grid/ui/setup/grid-env.sh ; source /nfs/soft/crab/setup/crab.sh
cmsenv

dir=Final
if [[ ! -d ${dir} ]]
then
    mkdir ${dir}
fi

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
echo "struct fo the NN is "$3
struct=$3
echo "number of iterations is "$4
iter=$4
echo "extra cuts are "$5
s_cuts=$5

root -l -b > ${dir}/logroot_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt << EOF

TString channel("${channel}")
TString mass("${mass}")
TString struct("${struct}")
TString iter("${iter}") 
TString s_cuts("${s_cuts}")
TString DIR("/nfs/user/acaudron/Tree2_537/");
TString fDY("Tree_rdsME_DY_"+channel+"_MC.root")
TString fTT("Tree_rdsME_TT-FullLept_"+channel+"_MC.root")
TString fZZ("Tree_rdsME_ZZ_"+channel+"_MC.root")
TString fZH("Tree_rdsME_ZH"+mass+"_"+channel+"_MC.root")

cout<<"Directory is "<<DIR<<endl;

// Output name
TString NN("ZH"+mass+"_"+channel+struct+"_"+iter+"_"+s_cuts);
cout<<" OUTPUT NAME : "<<NN<<endl;

// Structure of the NN and nbr of iteration
TString NNStruct0=struct.ReplaceAll("-",":");
TString NNStruct=NNStruct0.ReplaceAll("_",",@");
int iterations=$4;
cout<<"NNStruct "<<NNStruct<<endl;
cout<<"iterations "<<iterations<<endl;

//choose the cuts
TString cuts("")
if(s_cuts.Contains("Mbb80-160")) cuts+=" && (eventSelectiondijetM>80 && eventSelectiondijetM<160)";
if(s_cuts.Contains("Mbb50-160")) cuts+=" && (eventSelectiondijetM>50 && eventSelectiondijetM<160)";
if(s_cuts.Contains("Ptb1j40")) cuts+=" && jetmetbjet1pt>40";
if(s_cuts.Contains("Ptb2j25")) cuts+=" && jetmetbjet2pt>25";
if(s_cuts.Contains("Ptb2j25")) cuts+=" && eventSelectiondphiZbb>1.5";
if(s_cuts.Contains("Nj2")) cuts+=" && jetmetnj==2";
if(s_cuts.Contains("Nj3")) cuts+=" && jetmetnj>2";
if(s_cuts.Contains("Ptll20")) cuts+=" && (eventSelectionbestzptMu>20 || eventSelectionbestzptEle>20)";
cout<<"extra cuts : "<<cuts<<endl;

// Compilation and submission
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/include.h
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/Read_input_NN_inputs.h 
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/Generic_NN_higgs_NN_inputs.C+

Neural_net_E(DIR+fDY,DIR+fTT,DIR+fZZ,DIR+fZH,NN,NNStruct,iterations,cuts)

.q

EOF

grep Epoch ${dir}/logroot_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' > ${dir}/epoch_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt

NUMOFPOINTS=$(cat ${dir}/epoch_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b ${dir}/NN*${mass}*${channel}*${struct}*${iter}*${s_cuts}.root << EOF

//This part is copy and paste from the first time we call root

TString channel("${channel}")
TString mass("${mass}")
TString struct("${struct}")
TString iter("$iter") 
TString s_cuts("${s_cuts}")
TString dir("${dir}/")
TString NN("ZH"+mass+"_"+channel+struct+"_"+iter+"_"+s_cuts);

int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;

TString epochinputtxt = dir+"epoch_"+mass+"_"+channel+struct+"_"+iter+"_"+s_cuts+".txt";

TFile* foutput = TFile::Open(dir+"NN_Higgs_vs_Bkg_"+NN+".root","UPDATE");

.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/ComputeGraphFromTrainTxt.C
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
EOF

echo ${dir}/NN_Higgs_vs_Bkg_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.root
python doNorm.py ${dir}/NN_Higgs_vs_Bkg_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.root
cat CSV_nosys_test.txt | sed -e s%ROOTFILE%~acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/${dir}/NN_Higgs_vs_Bkg_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.root%g > ${dir}/CSV_nosys_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.txt
cat CSV_nosys_test.txt | sed -e s%ROOTFILE%~acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/${dir}/NN_Higgs_vs_Bkg_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.root%g | sed -e s%Combined/%Combined/prod%g > ${dir}/CSV_nosys_prod_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.txt

cd /home/fynu/acaudron/scratch/CMSSW_6_1_1/src
cmsenv
echo COMPUTE LIMIT FOR FINAL NN
combine -M Asymptotic ~acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/${dir}/CSV_nosys_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.txt -m 125 -t -1
echo END COMPUTE LIMIT FOR FINAL NN
echo ------------------------------------------------------------------------------------------------------------------

echo ------------------------------------------------------------------------------------------------------------------
echo COMPUTE LIMIT FOR PROD INTERMEDIATE NNs
combine -M Asymptotic ~acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/${dir}/CSV_nosys_prod_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.txt -m 125 -t -1
echo END COMPUTE LIMIT FOR PROD INTERMEDIATE NNs
echo ------------------------------------------------------------------------------------------------------------------
cd /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN
cmsenv