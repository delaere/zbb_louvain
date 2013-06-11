#! /bin/sh
HOME=~acaudron/
dirNN=~acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/ME_Analysis/MW_Analysis/NN_AN
cd ${dirNN}
source /nfs/soft/cms/cmsset_default.sh; export SCRAM_ARCH=slc5_amd64_gcc462 ; source /nfs/soft/grid/ui/setup/grid-env.sh ; source /nfs/soft/crab/setup/crab.sh
cmsenv

dir=FinalV3
if [[ ! -d ${dir} ]]
then
    mkdir ${dir}
fi

#Check for correct number of arguments
if [ $# -lt 5 ]
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
echo "NN choice is "$5
choice=$5
echo "extra cuts are "$6
s_cuts=$6

root -l -b > ${dir}/logroot_${choice}_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt << EOF

TString channel("${channel}")
TString mass("${mass}")
TString struct("${struct}")
TString iter("${iter}") 
TString s_cuts("${s_cuts}")
TString DIR("/nfs/user/acaudron/Tree2_537/");
TString outdir("${dir}")
TString choice("${choice}")
TString fZbb(DIR+"Tree_rdsME_Zbb_"+channel+"_MC.root")
TString fDY(DIR+"Tree_rdsME_DY_"+channel+"_MC.root")
TString fTTFullLept(DIR+"Tree_rdsME_TT-FullLept_"+channel+"_MC.root")
TString fTT(DIR+"Tree_rdsME_TT_"+channel+"_MC.root")
TString fZZ(DIR+"Tree_rdsME_ZZ_"+channel+"_MC.root")
TString fZH(DIR+"Tree_rdsME_ZH"+mass+"_"+channel+"_MC.root")

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
if(s_cuts.Contains("Mbb80-150")) cuts+=" && (eventSelectiondijetM>80 && eventSelectiondijetM<150)";
if(s_cuts.Contains("Mbb50-150")) cuts+=" && (eventSelectiondijetM>50 && eventSelectiondijetM<150)";
if(s_cuts.Contains("Mbb50-160")) cuts+=" && (eventSelectiondijetM>50 && eventSelectiondijetM<160)";
if(s_cuts.Contains("Ptb1j45")) cuts+=" && jetmetbjet1pt>45";
if(s_cuts.Contains("Ptb1j40")) cuts+=" && jetmetbjet1pt>40";
if(s_cuts.Contains("Ptb2j25")) cuts+=" && jetmetbjet2pt>25";
if(s_cuts.Contains("Ptb2j20")) cuts+=" && jetmetbjet2pt>20";
if(s_cuts.Contains("dPhiZbb1v7")) cuts+=" && eventSelectiondphiZbb>1.7";
if(s_cuts.Contains("Nj2")) cuts+=" && jetmetnj==2";
if(s_cuts.Contains("Nj3")) cuts+=" && jetmetnj>2";
if(s_cuts.Contains("prodNNs0v1")) cuts+=" && ProdNN>0.1";
if(s_cuts.Contains("Ptll20")) cuts+=" && (eventSelectionbestzptMu>20 || eventSelectionbestzptEle>20)";
cout<<"extra cuts : "<<cuts<<endl;

// Compilation and submission
.L ./include.h
.L ./Read_input_NN_inputs.h 
.L ./Generic_NN_higgs_NN_inputs.C+

Neural_net_E(fDY.Data(),fZbb.Data(),fTT.Data(),fTTFullLept.Data(),fZZ.Data(),fZH.Data(),NN,outdir,choice,NNStruct,iterations,cuts)

.q

EOF

grep Epoch ${dir}/logroot_${choice}_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' > ${dir}/epoch_${choice}_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt

NUMOFPOINTS=$(cat ${dir}/epoch_${choice}_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b ${dir}/NN*${choice}*${mass}*${channel}*${struct}*${iter}*${s_cuts}.root << EOF

//This part is copy and paste from the first time we call root

TString channel("${channel}")
TString mass("${mass}")
TString struct("${struct}")
TString iter("$iter") 
TString s_cuts("${s_cuts}")
TString dir("${dir}/")
TString choice("${choice}")
TString NN("ZH"+mass+"_"+channel+struct+"_"+iter+"_"+s_cuts);

int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;

TString epochinputtxt = dir+"epoch_"+choice+"_"+mass+"_"+channel+struct+"_"+iter+"_"+s_cuts+".txt";

TFile* foutput = TFile::Open(dir+"NN_"+choice+"_"+NN+".root","UPDATE");

.L ./ComputeGraphFromTrainTxt.C
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
EOF

echo ${dir}/NN_${choice}_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.root
python doNorm.py ${dir}/NN_${choice}_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.root
cat CSV_nosys_test.txt | sed -e s%ROOTFILE%${dirNN}/${dir}/NN_${choice}_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.root%g > ${dir}/CSV_nosys_${choice}_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.txt
cat CSV_nosys_test.txt | sed -e s%ROOTFILE%${dirNN}/${dir}/NN_${choice}_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.root%g | sed -e s%Channel/%Channel/prod%g > ${dir}/CSV_nosys_prod_${choice}_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.txt

cd ~acaudron/scratch/CMSSW_6_1_1/src
cmsenv
echo COMPUTE LIMIT FOR FINAL NN
combine -M Asymptotic ${dirNN}/${dir}/CSV_nosys_${choice}_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.txt -m 125 -t -1 > ${dirNN}/${dir}/loglimitNN_${choice}_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt
rm roostats*
echo END COMPUTE LIMIT FOR FINAL NN
echo ------------------------------------------------------------------------------------------------------------------

if [ ${choice} = "Higgs_vs_Bkg" ]
then
    echo ------------------------------------------------------------------------------------------------------------------
    echo COMPUTE LIMIT FOR PROD INTERMEDIATE NNs
    combine -M Asymptotic ${dirNN}/${dir}/CSV_nosys_prod_${choice}_ZH${mass}_${channel}${struct}_${iter}_${s_cuts}.txt -m 125 -t -1 > ${dirNN}/${dir}/loglimitProd_${choice}_${mass}_${channel}${struct}_${iter}_${s_cuts}.txt
    rm roostats*
    echo END COMPUTE LIMIT FOR PROD INTERMEDIATE NNs
    echo ------------------------------------------------------------------------------------------------------------------
fi

cd ${dirNN}
cmsenv