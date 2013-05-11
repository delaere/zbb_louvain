
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
arguments = comb 125 3_2_3 5000
queue

# run the program
arguments = comb 125 3_2 5000
queue

# run the program
arguments = comb 125 5_2_3 5000
queue

# run the program
arguments = comb 125 2_4 5000
queue

# run the program
arguments = comb 125 4_6_2 5000
queue

# run the program
arguments = comb 125 6 5000
queue

# run the program
arguments = comb 125 2_3_2 5000
queue

# run the program
arguments = comb 125 2_5_3 5000
queue

# run the program
arguments = comb 125 8_5_3 5000
queue

# run the program
arguments = comb 125 8_5_3 5000
queue

# run the program
arguments = comb 125 10_7_5_3 5000
queue

# run the program
arguments = comb 125 7_10_3 5000
queue

# run the program
arguments = comb 125 1 5000
queue

# run the program
arguments = comb 125 2 5000
queue

# run the program
arguments = comb 125 3 5000
queue