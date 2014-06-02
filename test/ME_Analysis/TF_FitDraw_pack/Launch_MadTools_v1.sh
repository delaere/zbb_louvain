#! /bin/sh

echo hello good luck

root -l -b << EOF

gSystem->Load("libPhysics")
gSystem->Load("libEG")

.L classes.C+
.L Cpp/Likelihood_minmisation.C+
//.L Cpp/Draw.C+
.L Cpp/Draw2.C+

Likelihood_minmisation("../TF_data_tt_Electron.root")
//Likelihood_minmisation("../TF_data_tt.root")

// 	DATA         ;	parameters_Delphe_14    ;LV ;UV;Xgs;D_min;D_max

//Draw("File/output_merged.root","File/parameters.txt",0,90,4,-100,100,0)
//Draw("File/output_merged.root","File/parameters.txt",90,150,4,-200,200,1)
//Draw("File/output_merged.root","File/parameters.txt",180,300,8,-200,200,2)
//Draw("File/output_merged.root","File/parameters.txt",300,1000,16,-200,200,3)

Draw("/home/fynu/tdupree/scratch/testTF_532/CMSSW_5_3_2_patch4/src/UserCode/zbb_louvain/python/outCMStoTFstudyMU_PTINV_0.root","File/parameters_mu.txt",15,90,1,-0.005,0.005,0)
Draw("/home/fynu/tdupree/scratch/testTF_532/CMSSW_5_3_2_patch4/src/UserCode/zbb_louvain/python/outCMStoTFstudyMU_PTINV_0.root","File/parameters_mu.txt",90,150,1,-0.005,0.005,1)
Draw("/home/fynu/tdupree/scratch/testTF_532/CMSSW_5_3_2_patch4/src/UserCode/zbb_louvain/python/outCMStoTFstudyMU_PTINV_0.root","File/parameters_mu.txt",180,300,1,-0.005,0.005,2)
Draw("/home/fynu/tdupree/scratch/testTF_532/CMSSW_5_3_2_patch4/src/UserCode/zbb_louvain/python/outCMStoTFstudyMU_PTINV_0.root","File/parameters_mu.txt",300,1000,1,-0.005,0.005,3)


.q


EOF

