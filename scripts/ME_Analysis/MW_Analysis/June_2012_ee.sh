#! /bin/sh
echo
echo --------------------------------------------------------------------------------------------------------------------------------------------
echo 																		
echo ------------ Hello $USER -----------------------												
echo 																		
echo --------- input File--------------														
echo  ggToZbb Weight   : /home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/gg_Zbb_ee_2505012/Events/JUNE_12_ $1 0/JUNE_12_ $1 0_weights.out
echo  qqToZbb Weight   : /home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/qq_Zbb_ee_2505012/Events/JUNE_12_ $1 0/JUNE_12_$1 0_weights.out
echo  ttbar   Weights  : /home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/tt_ee_2505012/Events/JUNE_12_ $1 2/JUNE_12_$1 2_weights.out
echo  zz C0 Weight   : /home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/ZZ_C0_ee_2505012/Events/JUNE_12_ $1 0/JUNE_12_$1 0_weights.out
echo  zz C3 Weight   : /home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/ZZ_C3_ee_2505012/Events/JUNE_12_ $1 3/JUNE_12_$1 3_weights.out
echo  zh C0 Weight   : /home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/ZH_C0_ee_2505012/Events/JUNE_12_ $1 0/JUNE_12_$1 0_weights.out
echo  zh C3 Weight   :/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/ZH_ee_250512/Events/JUNE_12_ $1 3/JUNE_12_"$1 3_weights.out
echo  twb Weight   : /home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/twb_ee_2505012/Events/JUNE_12_ $1 2/JUNE_12_$1 2_weights.out
echo  LHCO file info   : /home/fynu/arnaudp/scratch/MW_5/inputFiles/JUNE_12/$2				
echo  Event info       : /home/fynu/arnaudp/scratch/MW_5/inputFiles/JUNE_12/$3 									

echo -------- Sample info -------------													
echo  output name      : $1														
echo -------- Sample info -------------													
echo  is D-Y            = $5  0 or 1													
echo  channel           = $6  0 ee --- 1 mumu												
echo  Event to process  - $4														
echo -------- Executable ---------------												
echo       MW_analysis_All_Full_v4.C														
echo
echo --------------------------------------------------------------------------------------------------------------------------------------------

echo
echo ---- Do you want to submit this job ? yes - no  -------
echo
read tag
echo
echo $tag

if [ "$tag" = "yes" ] ; then

root -l -b << EOF

gSystem->Load("libPhysics")
gSystem->Load("libEG")
gSystem->Load("ExRootAnalysis/lib/libExRootAnalysis.so")

TString file("$1")
TString file2("$2")
TString file3("$3")

TString qq("/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/gg_Zbb_ee_2505012/Events/JUNE_12_"+file+"0/JUNE_12_"+file+"0_weights.out");
TString gg("/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/qq_Zbb_ee_2505012/Events/JUNE_12_"+file+"0/JUNE_12_"+file+"0_weights.out");
TString tt("/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/tt_ee_2505012/Events/JUNE_12_"+file+"2/JUNE_12_"+file+"2_weights.out");
TString zz_c0("/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/ZZ_C0_ee_2505012/Events/JUNE_12_"+file+"0/JUNE_12_"+file+"0_weights.out");
TString zz_c3("/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/ZZ_C3_ee_2505012/Events/JUNE_12_"+file+"3/JUNE_12_"+file+"3_weights.out");
TString hi_c0("/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/ZH_C0_ee_2505012/Events/JUNE_12_"+file+"0/JUNE_12_"+file+"0_weights.out");
TString hi_c3("/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/ZH_ee_250512/Events/JUNE_12_"+file+"3/JUNE_12_"+file+"3_weights.out");
TString twb("/home/fynu/arnaudp/scratch/MW_5/new_madweight/madweight/twb_ee_2505012/Events/JUNE_12_"+file+"2/JUNE_12_"+file+"2_weights.out");

TString LHCO("/home/fynu/arnaudp/scratch/MW_5/inputFiles/JUNE_12/")
TString EvtInfo("/home/fynu/arnaudp/scratch/MW_5/inputFiles/JUNE_12/")

.L include.h
.L MW_analysis_All_Full_v4.C+ 

MWToRoot(gg,qq,tt,twb,zz_c3,zz_c0,hi_c3,hi_c0,LHCO+file2,EvtInfo+file3,file,$4,$5,$6)

.q

EOF

fi
