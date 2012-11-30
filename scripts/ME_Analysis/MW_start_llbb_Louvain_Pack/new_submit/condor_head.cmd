# here goes your shell script
executable     = new_submit/worker.sh

# here you specify where to put .log, .out and .err files
output         = /dev/null
error          = /dev/null
log            = /dev/null

# the following two parameters enable the file transfer mechanism
# and specify that the output files should be transferred back
# to the submit machine from the remote machine where the job executes
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT

# the following two parameters are required for the ingrid cluster
universe       = vanilla
requirements   = (CMSFARM =?= TRUE)
# for Madgraph users replace the previous line by:
#requirements   = (MADGRAPH =?= TRUE)


