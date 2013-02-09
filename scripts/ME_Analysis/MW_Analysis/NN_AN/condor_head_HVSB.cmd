
# here goes your shell script
executable     = NN_June_HiggsVSBkg.sh

# here you specify where to put .log, .out and .err files
output         = condor/condor.out.$(Cluster).$(Process)
error          = condor/condor.err.$(Cluster).$(Process)
log            = condor/condor.log.$(Cluster).$(Process)

# the following two parameters enable the file transfer mechanism
# and specify that the output files should be transferred back
# to the submit machine from the remote machine where the job executes
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT

# the following two parameters are required for the ingrid cluster
universe       = vanilla
#requirements   = (CMSFARM =?= TRUE)
# for Madgraph users replace the previous line by:
requirements   = (MADGRAPH =?= TRUE)

# run the program
arguments = 120 comb
queue

# arguments = 2 2 comb
# queue

# arguments = 3 2 comb
# queue
