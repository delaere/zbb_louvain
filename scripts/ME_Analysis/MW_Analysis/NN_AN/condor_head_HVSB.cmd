
# here goes your shell script
executable     = NN_June_HVSB.sh

# here you specify where to put .log, .out and .err files
output         = condor/condor.out.$(Cluster).$(Process)
error          = condor/condor.err.$(Cluster).$(Process)
log            = condor/condor.log.$(Cluster).$(Process)

# the following two parameters enable the file transfer mechanism
# and specify that the output files should be transferred back
# to the submit machine from the remote machine where the job executes
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT

transfer_input_files=include.h,Read_input.h,Read_input_NN_inputs.h,Generic_NN_higgs_test.C,Generic_NN_higgs_NN_inputs.C,ComputeGraphFromTrainTxt.C,MLP_Higgs_vs_DY_ML_CSV_2011_comb_ZH125_multi2.cxx,MLP_Higgs_vs_DY_ML_CSV_2011_comb_ZH125_multi2.h,MLP_Higgs_vs_DY_ML_CSV_2011_comb_ZH125_multiPlus2.cxx,MLP_Higgs_vs_DY_ML_CSV_2011_comb_ZH125_multiPlus2.h,MLP_Higgs_vs_TT_ML_CSV_2011_comb_ZH125_multi2.cxx,MLP_Higgs_vs_TT_ML_CSV_2011_comb_ZH125_multi2.h,MLP_Higgs_vs_TT_ML_CSV_2011_comb_ZH125_multiPlus2.cxx,MLP_Higgs_vs_TT_ML_CSV_2011_comb_ZH125_multiPlus2.h,MLP_Higgs_vs_ZZ_ML_CSV_2011_comb_ZH125_multi2.cxx,MLP_Higgs_vs_ZZ_ML_CSV_2011_comb_ZH125_multi2.h,MLP_Higgs_vs_ZZ_ML_CSV_2011_comb_ZH125_multiPlus2.cxx,MLP_Higgs_vs_ZZ_ML_CSV_2011_comb_ZH125_multiPlus2.h

# the following two parameters are required for the ingrid cluster
universe       = vanilla
requirements   = (CMSFARM =?= TRUE)
# for Madgraph users replace the previous line by:
#requirements   = (MADGRAPH =?= TRUE)

# run the program
arguments = multi2
queue

arguments = multiPlus2
queue

