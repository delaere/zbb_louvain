
f = open('generatedZZvsBkg.cmd', 'w')

f.write(
    '# here goes your shell script\n'
    'executable     = NN_June_HiggsVSBkg.sh\n'
    '\n'
    '# here you specify where to put .log, .out and .err files\n'
    'output         = condor/condor.out.$(Cluster).$(Process)\n'
    'error          = condor/condor.err.$(Cluster).$(Process)\n'
    'log            = condor/condor.log.$(Cluster).$(Process)\n'
    '\n'
    '# the following two parameters enable the file transfer mechanism\n'
    '# and specify that the output files should be transferred back\n'
    '# to the submit machine from the remote machine where the job executes\n'
    'should_transfer_files   = YES\n'
    'when_to_transfer_output = ON_EXIT\n'
    '\n'
    '# the following two parameters are required for the ingrid cluster\n'
    'universe       = vanilla\n'
    'requirements   = (CMSFARM =?= TRUE)\n'
    '# for Madgraph users replace the previous line by:\n'
    '#requirements   = (MADGRAPH =?= TRUE)\n'
    '\n'
    )
    
struct = [
    #'-1',
    '-2',
    '-3',
    '-4',
    '-5',
    #'-6',
    #'-7',
    #'-8',
    #'-9',
    #'-2-2',
    #'-2-3',
    #'-2-4',
    '-3-2',
    '-3-3',
    #'-3-4',
    #'-3-5',
    #'-3-6',
    '-4-2',
    '-4-3',
    '-4-4',
    #'-4-5',
    #'-4-6',
    #'-5-2',
    '-5-3',
    '-5-4',
    #'-5-5',
    #'-5-6',
    #'-6-2',
    #'-6-3',
    #'-6-4',
    #'-6-5',
    #'-6-6',
    #'-9-2',
    #'-9-3',
    #'-9-4',
    #'-9-5',
    #'-9-6',
    #'-2-2-2',
    #'-2-3-2',
    #'-2-3-3',
    #'-2-4-2',
    #'-2-4-3',
    #'-2-4-4',
    #'-3-2-2',
    #'-3-2-3',
    #'-3-3-2',
    #'-3-3-3',
    #'-3-4-2',
    #'-3-4-3',
    #'-3-4-4',
    #'-3-5-2',
    #'-3-5-3',
    #'-3-5-4',
    #'-3-5-5',
    #'-3-6-2',
    #'-3-6-3',
    #'-3-6-4',
    #'-3-6-5',
    #'-3-6-6',
    #'-4-2-2',
    #'-4-2-3',
    #'-4-2-4',
    #'-4-3-2',
    #'-4-3-3',
    #'-4-3-4',
    #'-4-4-2',
    #'-4-4-3',
    #'-4-4-4',
    #'-4-5-2',
    #'-4-5-3',
    #'-4-5-4',
    #'-4-5-5',
    #'-4-6-2',
    #'-4-6-3',
    #'-4-6-4',
    #'-4-6-5',
    #'-5-2-2',
    #'-5-2-3',
    #'-5-2-4',
    #'-5-3-2',
    #'-5-3-3',
    #'-5-3-4',
    #'-5-3-5',
    #'-5-4-2',
    #'-5-4-3',
    #'-5-4-4',
    #'-5-4-5',
    #'-5-5-2',
    #'-5-5-3',
    #'-5-5-4',
    #'-5-5-5',
    #'-6-2-2',
    #'-6-2-3',
    #'-6-2-4',
    #'-6-3-2',
    #'-6-3-3',
    #'-6-3-4',
    #'-6-3-5',
    #'-6-4-2',
    #'-6-4-3',
    #'-6-4-4',
    #'-6-4-5',
    #'-6-5-2',
    #'-6-5-3',
    ##'-6-5-4',
    ##'-6-5-5',
    #'-6-6-2',
    #'-6-6-3',
    ##'-6-6-4',
    ##'-6-6-5',
    #'-9-2-2',
    #'-9-2-3',
    #'-9-2-4',
    #'-9-3-2',
    #'-9-3-3',
    #'-9-3-4',
    #'-9-3-5',
    ##'-9-4-2',
    ##'-9-4-3',
    #'-9-4-4',
    #'-9-4-5',
    #'-9-5-2',
    #'-9-5-3',
    #'-9-5-4',
    #'-9-5-5',
    #'-9-6-2',
    #'-9-6-3',
    #'-9-6-4',
    #'-9-6-5',
    ]

iter = [
    '100',
    '300',
    '500',
    '750',
    '1000',
    #'1750',
    #'2500',
    #'5000',
    #'7500',
    #'10000',
    #'1000',
    ]

vars = [
    '',
    #'_trijetMdr_fsrDR',
    #'_Mbb',
    #'_regMbb',
    '_prodCSV',
    #'_prodNNs2j',
    #'_prodNNs3j',
    ]

cuts = [
    #'Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20',
    #'Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20',
    'Nj2_Mbb45-115_Ptb1j40_Ptb2j25_Ptll20',
    'Nj3_Mbb15-115_Ptb1j40_Ptb2j25_Ptll20',
    ]

NN = {
    #'Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20' : 'Higgs_vs_Bkg_2j',
    #'Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20' : 'Higgs_vs_Bkg_3j',
    #'Nj2_Mbb45-115_Ptb1j40_Ptb2j25_Ptll20' : 'ZZ_vs_DY',
    #'Nj3_Mbb15-115_Ptb1j40_Ptb2j25_Ptll20' : 'ZZ_vs_DY',
    #'Nj2_Mbb45-115_Ptb1j40_Ptb2j25_Ptll20' : 'ZZ_vs_TT',
    #'Nj3_Mbb15-115_Ptb1j40_Ptb2j25_Ptll20' : 'ZZ_vs_TT',
    'Nj2_Mbb45-115_Ptb1j40_Ptb2j25_Ptll20' : 'ZZ_vs_Bkg_2j',
    'Nj3_Mbb15-115_Ptb1j40_Ptb2j25_Ptll20' : 'ZZ_vs_Bkg_3j',
    }
for s in struct :
    for v in vars :
        for c in cuts :
            if (v=="_prodNNs3j" or v=="_trijetMdr_fsrDR") and "Nj2" in c : continue
            if v=="_prodNNs2j" and "Nj3" in c : continue
            #if v=="" and "Nj3" in c : continue
            for i in iter :
                f.write(
                    '########################structure '+v+s+' ###################################\n'
                    '# run the program\n'
                    'arguments = comb 125 '+v+s+' '+i+' '+NN[c]+' '+c+'\n'
                    'queue\n'
                    '\n'
                    )
