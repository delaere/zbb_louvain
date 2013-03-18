#script to create the working directories for each process
#higgs dir. are splited in 3 as there is 9 higgs mass hypo. to evaluate

./bin/mg5 << +EOF

### mumu ####

#### gg to Zbb ####
define q = u c d s u~ c~ d~ s~
generate g g > z b b~ , z > mu+ mu-
output madweight ggZbb_mumu

### qq to Zbb ####
generate q q > z b b~ , z > mu+ mu-
output madweight qqZbb_mumu

### ttbar ####
define p = g u c d s u~ c~ d~ s~
generate p p > t t~ , ( t > b w+ , w+ > mu+ vm ) , ( t~ > b~ w- , w- > mu- vm~ )
output madweight ttbar_mumu

### zz_C0 #####
define p = g u c d s u~ c~ d~ s~
generate p p > z z , z > mu+ mu- , z > b b~
output madweight ZZ_C0_mumu

### zz_C3 #####
define p = g u c d s u~ c~ d~ s~
generate p p > z z , z > mu+ mu- , z > b b~
output madweight ZZ_C3_mumu

#### zh_C0_123 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > mu+ mu- , h > b b~
output madweight ZH_C0_123_mumu

#### zh_C3_123 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > mu+ mu- , h > b b~
output madweight ZH_C3_123_mumu

#### zh_C0_456 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > mu+ mu- , h > b b~
output madweight ZH_C0_456_mumu

#### zh_C3_456 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > mu+ mu- , h > b b~
output madweight ZH_C3_456_mumu

#### zh_C0_789 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > mu+ mu- , h > b b~
output madweight ZH_C0_789_mumu

#### zh_C3_789 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > mu+ mu- , h > b b~
output madweight ZH_C3_789_mumu


### elel ####

#### gg to Zbb ####
define q = u c d s u~ c~ d~ s~
generate g g > z b b~ , z > e+ e-
output madweight ggZbb_ee

### qq to Zbb ####
generate q q > z b b~ , z > e+ e-
output madweight qqZbb_ee

### ttbar ####
define p = g u c d s u~ c~ d~ s~
generate p p > t t~ , ( t > b w+ , w+ > e+ ve ) , ( t~ > b~ w- , w- > e- ve~ )
output madweight ttbar_ee

### zz_C0_123 #####
define p = g u c d s u~ c~ d~ s~
generate p p > z z , z > e+ e- , z > b b~
output madweight ZZ_C0_123_ee

### zz_C3_123 #####
define p = g u c d s u~ c~ d~ s~
generate p p > z z , z > e+ e- , z > b b~
output madweight ZZ_C3_123_ee

#### zh_C0_456 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > e+ e- , h > b b~
output madweight ZH_C0_456_ee

#### zh_C3_456 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > e+ e- , h > b b~
output madweight ZH_C3_456_ee

#### zh_C0_789 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > e+ e- , h > b b~
output madweight ZH_C0_789_ee

#### zh_C3_789 ####
define p = g u c d s u~ c~ d~ s~
generate p p > z h , z > e+ e- , h > b b~
output madweight ZH_C3_789_ee

exit()

+EOF
