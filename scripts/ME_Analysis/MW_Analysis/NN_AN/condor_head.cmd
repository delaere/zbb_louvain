
# here goes your shell script
executable     = NN_June.sh

# here you specify where to put .log, .out and .err files
output         = condor/condor.out.$(Cluster).$(Process)
error          = condor/condor.err.$(Cluster).$(Process)
log            = condor/condor.log.$(Cluster).$(Process)

# the following two parameters enable the file transfer mechanism
# and specify that the output files should be transferred back
# to the submit machine from the remote machine where the job executes
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT

transfer_input_files=include.h,Read_input.h,Read_input_NN_inputs_m.h,Generic_NN_higgs_test.C,Generic_NN_higgs_NN_inputs_m.C,ComputeGraphFromTrainTxt.C

# the following two parameters are required for the ingrid cluster
universe       = vanilla
requirements   = (CMSFARM =?= TRUE)
# for Madgraph users replace the previous line by:
#requirements   = (MADGRAPH =?= TRUE)

# run the program
arguments = DY ML comb 125 multi2 4:3 800
queue

arguments = DY ML comb 125 multiPlus2 7:4 5000
queue

arguments = TT ML comb 125 multi2 4:3 2000
queue

arguments = TT ML comb 125 multiPlus2 7:4 5000
queue

arguments = ZZ ML comb 125 multi2 4:3 2000
queue

arguments = ZZ ML comb 125 multiPlus2 4:3 1000
queue

