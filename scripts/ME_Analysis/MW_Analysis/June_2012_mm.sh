#! /bin/sh
echo
echo --------------------------------------------------------------------------------------------------------------------------------------------
echo 																		
echo ------------ Hello $USER -----------------------												
echo 																		
echo --------- input File--------------														
echo  ggToZbb Weight   : /home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/qqtozbb_mm_june2012/Events/$1                                                     
echo  qqToZbb Weight   : /home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ggtozbb_mm_june2012/Events/$1                                                     
echo  ttbar   Weights  : /home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/tt_mm_june2012/Events/$1                                          
echo  zz C0 Weight   : /home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ZZ_mm_june2012/Events/$1                                                   
echo  zz C3 Weight   : /home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ZZ_mm_june2012/Events/$1
echo  zh C0 Weight   : /home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ZH_mm_june2012/Events/$1                                                   
echo  zh C3 Weight   : /home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ZH_mm_june2012/Events/$1
echo  twb Weight   : /home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/tW_mm_june2012/Events/$1
echo  LHCO file info   :/home/fynu/cbeluffi/scratch/MW_5/madweight/MW_Analysis/inputFiles/$2                            
echo  Event info       :/home/fynu/cbeluffi/scratch/MW_5/madweight/MW_Analysis/inputFiles/$3 
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

TString qq("/home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/qqtozbb_mm_june2012/Events/JUNE_12_"+file+"0/JUNE_12_"+file+"0_weights.out");
TString gg("/home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ggtozbb_mm_june2012/Events/JUNE_12_"+file+"0/JUNE_12_"+file+"0_weights.out");
TString tt("/home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/tt_mm_june2012/Events/JUNE_12_"+file+"2/JUNE_12_"+file+"2_weights.out");
TString zz_c0("/home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ZZ_mm_june2012/Events/JUNE_12_"+file+"0/JUNE_12_"+file+"0_weights.out");
TString zz_c3("/home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ZZ_mm_june2012/Events/JUNE_12_"+file+"3/JUNE_12_"+file+"3_weights.out");
TString hi_c0("/home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ZH_mm_june2012/Events/JUNE_12_"+file+"0/JUNE_12_"+file+"0_weights.out");
TString hi_c3("/home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/ZH_mm_june2012/Events/JUNE_12_"+file+"3/JUNE_12_"+file+"3_weights.out");
TString twb("/home/fynu/cbeluffi/scratch/MW_5/June_2012/madweight/tW_mm_june2012/Events/JUNE_12_"+file+"2/JUNE_12_"+file+"2_weights.out");

TString LHCO("/home/fynu/cbeluffi/scratch/MW_5/madweight/MW_Analysis/inputFiles/")
TString EvtInfo("/home/fynu/cbeluffi/scratch/MW_5/madweight/MW_Analysis/inputFiles/")

.L include.h
.L MW_analysis_All_Full_v4.C+ 

MWToRoot(gg,qq,tt,twb,zz_c3,zz_c0,hi_c3,hi_c0,LHCO+file2,EvtInfo+file3,file,$4,$5,$6)

.q

EOF

fi
