#! /bin/sh

echo ----------- Hello $USER -----------------------

echo $1
echo $2
echo $3
echo $4
root -l -b << EOF

gSystem->Load("libPhysics")
gSystem->Load("libEG")

TString File("/home/fynu/arnaudp/scratch/MW_5/inputFiles/JUNE_12/");
TString f1("$1")
TString f2("$2")
TString f3("$3")
TString f4("$4")
TString f5("$5")
TString f6("$6")
TString NN("XXX")

.L include.h
.L Read_input.h
.L Generic_NN.C+ 

Neural_net_E(File+f1,File+f2,File+f3,File+f4,File+f5,File+f6,$7,$8,$9,$10,$11,$12,NN)

.q

EOF
