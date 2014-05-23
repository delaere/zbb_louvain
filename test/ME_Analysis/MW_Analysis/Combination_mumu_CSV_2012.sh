#! /bin/sh
#./Combination_mumu_CSV_2011.sh DY_mumu outCMStoLHCOEl_MC_CSV2012Sel_V2_0_LHCO.root outCMStoLHCOEl_MC_CSV2012Sel_V2_0.root 8645 1 0
echo
echo --------------------------------------------------------------------------------------------------------------------------------------------
echo 																		
echo ------------ Hello $USER -----------------------												
echo 																		
echo
echo --------- input File--------------														
echo
echo  ggToZbb Weight   : /home/fynu/acaudron/scratch/MWjobs/madweight/ggZbb_mumu/Events/$1/$1_weights.out
echo  qqToZbb Weight   : /home/fynu/acaudron/scratch/MWjobs/madweight/qqZbb_mumu/Events/$1/$1_weights.out
echo  ttbar   Weights  : /home/fynu/acaudron/scratch/MWjobs/madweight/ttbar_mumu/Events/$1/$1_weights.out
echo  zz C0 Weight   : /home/fynu/acaudron/scratch/MWjobs/madweight/ZZ_C0_mumu/Events/$1/$1_weights.out
echo  zz C3 Weight   : /home/fynu/acaudron/scratch/MWjobs/madweight/ZZ_C3_mumu/Events/$1/$1_weights.out
echo  zh C0 Weight   : /home/fynu/acaudron/scratch/MWjobs/madweight/ZH_C0_mumu/Events/$1/$1_weights.out
echo  zh C3 Weight   :/home/fynu/acaudron/scratch/MWjobs/madweight/ZH_C3_mumu/Events/$1/$1_weights.out 
echo  LHCO file info   : /nfs/user/acaudron/LHCO53X/$2				
echo  Event info       : /nfs/user/acaudron/LHCO53X/$3 									
echo
echo -------- Sample info -------------													
echo  output name      : $1														
echo -------- Sample info -------------													
echo  is D-Y            = $5  0 or 1													
echo  channel           = $6  0 ee --- 1 mumu												
echo  Event to process  - $4														
echo -------- Executable ---------------												
echo       MW_analysis_All_Full_v7.C														
echo
echo --------------------------------------------------------------------------------------------------------------------------------------------
echo
echo
echo ---- Do you want to submit this job ? yes - no  -------
echo
#read tag
echo
#echo $tag
tag="yes"
if [ "$tag" = "yes" ] ; then

root -l -b << EOF

gSystem->Load("libPhysics")
gSystem->Load("libEG")
gSystem->Load("ExRootAnalysis/lib/libExRootAnalysis.so")

TString file("$1")
TString file2("$2")
TString file3("$3")

TString gg("/home/fynu/acaudron/scratch/MWjobs/madweight/ggZbb_mumu/Events/"+file+"/"+file+"_weights.out");
TString qq("/home/fynu/acaudron/scratch/MWjobs/madweight/qqZbb_mumu/Events/"+file+"/"+file+"_weights.out");
TString tt("/home/fynu/acaudron/scratch/MWjobs/madweight/ttbar_mumu/Events/"+file+"/"+file+"_weights.out");
TString zz_c0("/home/fynu/acaudron/scratch/MWjobs/madweight/ZZ_C0_mumu/Events/"+file+"/"+file+"_weights.out");
TString zz_c3("/home/fynu/acaudron/scratch/MWjobs/madweight/ZZ_C3_mumu/Events/"+file+"/"+file+"_weights.out");
TString hi_c0("/home/fynu/acaudron/scratch/MWjobs/madweight/ZH_C0_mumu/Events/"+file+"/"+file+"_weights.out");
TString hi_c3("/home/fynu/acaudron/scratch/MWjobs/madweight/ZH_C3_mumu/Events/"+file+"/"+file+"_weights.out");
TString tt0("/home/fynu/acaudron/scratch/MWjobs/madweight/ttbar_C0_mumu/Events/"+file+"/"+file+"_weights.out");

TString LHCO("/nfs/user/acaudron/LHCO537/")
TString EvtInfo("/nfs/user/acaudron/LHCO537/")

.L include.h
.L MW_analysis.C+ 

MWToRoot(gg,qq,tt,tt0,zz_c3,zz_c0,hi_c3,hi_c0,LHCO+file2,EvtInfo+file3,file,$4,$5,$6)

.q

EOF

fi
