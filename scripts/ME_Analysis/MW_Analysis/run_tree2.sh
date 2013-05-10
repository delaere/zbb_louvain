##########################################################################################################################
##############################################Producing 2011 Tree 2##############################################
##########################################################################################################################


########################Configure MW_analysis_All_Full_v7.C ###################################################
#
#
#   If you run on anysample BUT ZH, run with 
#      (l.352) -> for (Int_t entry2 = 0; entry2 <allEntries; ++entry2){
#     instead of 
#      (l.353) -> for (Int_t entry2 = 0; entry2 <EventToProcess; ++entry2){
#
#   If you run on DATA, activate the run number matching l 387 :
#
#              -> if(eventNumber==EvtNum[jj]) && runNumber==RunNbr[jj]){
#      instead of  
#                 if(eventNumber==EvtNum[jj]){// && runNumber==RunNbr[jj]){
#
###############################################################################################################

# Also make sure that the LHCO run number is at 1 (0 1 1424223 for instance). The important point is that the second number is not a huge number.

######Explaination of the command############################################################################################################
#
#./Combination_ee_CSV_2011.sh name_of_the_MW_folders name_of_the_LHCO_file_converted_in_ROOT Tree1_file number_of_events isDY channel DYsample
# name_of_the_MW_folders -> check the name of yoyr MW instances and the corresponding path in Combination_ee_CSV_2011.sh
# name_of_the_LHCO_file_converted_in_ROOT -> Convert the LHCO file used for MW in a ROOT file (use ExRootAnalysis)
# Tree1_file -> Use the proper tree1 linked to the LHCO file
# number_of_events -> number of events in your sample
# isDY -> 0:no, 1:yes
# channel -> 0:ee, 1:mumu
# DYsample -> 0: Zbb4flavor, 1:DY inclusive, DY high pTZ
#
############################################################################################################################################


./Combination_ee_CSV_2011.sh TT_ee TT_ee_LHCO.root TT_ee.root 23432 0 0 -1
./Combination_mm_CSV_2011.sh TT_mm TT_mm_LHCO.root TT_mm.root 32021 0 1 -1
./Combination_mm_CSV_2011.sh DY_mm DY_mm_LHCO.root DY_mm.root 11729 1 1 1
./Combination_ee_CSV_2011.sh DY_ee DY_ee_LHCO.root DY_ee.root 8001 1 0 1
./Combination_ee_CSV_2011.sh DY_pt100_ee DY_Pt100_ee_LHCO.root DY_Pt100_ee.root 3054 1 0 2
./Combination_mm_CSV_2011.sh DY_pt100_mm DY_Pt100_mm_LHCO.root DY_Pt100_mm.root 4089 1 1 2
./Combination_mm_CSV_2011_camille.sh Zbb4F_mm Zbb4F_mu.root outRDStoLHCO_ZbbMG4F_Mu_MC.root 33339 1 1 0
./Combination_ee_CSV_2011_camille.sh Zbb4F_ee Zbb4F_el.root outRDStoLHCO_ZbbMG4F_El_MC.root 23190 1 0 0
./Combination_ee_CSV_2011.sh ZZ_ee ZZ_ee_LHCO.root ZZ_ee.root 5356 0 0 -1
./Combination_mm_CSV_2011.sh ZZ_mm ZZ_mm_LHCO.root ZZ_mm.root 7776 0 1 -1
#./Combination_mm_CSV_2011.sh ZH125_mm ZH_mm_m125_LHCO.root ZH_mm_m125.root 15584 0 1 -1
#./Combination_ee_CSV_2011.sh ZH125_ee ZH_ee_m125_LHCO.root ZH_ee_m125.root 13896 0 0 -1
#./Combination_ee_CSV_2011.sh ZH115_ee ZH_ee_m115_LHCO.root ZH_ee_m115.root 12753 0 0 -1
#./Combination_mm_CSV_2011.sh ZH115_mm ZH_mm_m115_LHCO.root ZH_mm_m115.root 14527 0 1 -1
#./Combination_mm_CSV_2011.sh ZH120_mm ZH_mm_m120_LHCO.root ZH_mm_m120.root 14807 0 1 -1
#./Combination_ee_CSV_2011.sh ZH120_ee ZH_ee_m120_LHCO.root ZH_ee_m120.root 13074 0 0 -1
#./Combination_ee_CSV_2011.sh ZH130_ee ZH_ee_m130_LHCO.root ZH_ee_m130.root 14222 0 0 -1
#./Combination_mm_CSV_2011.sh ZH130_mm ZH_mm_m130_LHCO.root ZH_mm_m130.root 16058 0 1 -1
#./Combination_mm_CSV_2011.sh ZH135_mm ZH_mm_m135_LHCO.root ZH_mm_m135.root 16404 0 1 -1
#./Combination_ee_CSV_2011.sh ZH135_ee ZH_ee_m135_LHCO.root ZH_ee_m135.root 14592 0 0 -1

./Combination_mm_CSV_2011.sh DataA_mm DataA_mm_LHCO.root DataA_mm.root 2218 0 1 -1
./Combination_mm_CSV_2011.sh DataB_mm DataB_mm_LHCO.root DataB_mm.root 2616 0 1 -1
./Combination_ee_CSV_2011.sh DataB_ee DataB_ee_LHCO.root DataB_ee.root 1962 0 0 -1
./Combination_ee_CSV_2011.sh DataA_ee DataA_ee_LHCO.root DataA_ee.root 1588 0 0 -1











