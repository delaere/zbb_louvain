from weightsMerging_Function import *

#JP or CSV bTag?
stringsToLookFor="JP"

#Directory of the MW instances
MW_directory="/home/fynu/cbeluffi/scratch/MW5_aug14/MG5_aMC_v2_1_2_beta2/"

#Directory where the input rootFiles are stored
directory="/home/fynu/cbeluffi/storage/RDS/5320_"+stringsToLookFor+"_Skimmed_V5/llbbX/"   

#Specify the stage corresponding to each channel you want to consider 
stages=["rc_stage_6_idx","rc_stage_16_idx"]

#{Name in the tree : [name of the different instances]}  CAREFUL : order and number of entries MUST correspond to the stages above, fill with "" for EMu if there is no DY_EMu instance
dict_InstanceNameInTree_ChannelNames = {"TT":["tt_mm","tt_ee"],
					"qq_Zbb":["qq_Zbb_mm","qq_Zbb_ee"],
					"gg_Zbb":["gg_Zbb_mm","gg_Zbb_ee"],
					"ZZ_cor0":["ZZ_cor0_mm","ZZ_cor0_ee"],
					"ZZ_cor3":["ZZ_cor3_mm","ZZ_cor3_ee"],
					"ZH_cor0":["ZH_cor0_mm","ZH_cor0_ee"],
					"ZH_cor3":["ZH_cor3_mm","ZH_cor3_ee"]
					} 

#{Name of the input rootFile :  Name of the directory in the MadWeight instances }
dict_Sample_nameInInstance={    "DoubleMu2012A_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DoubleA_2",
                                "DoubleMu2012B_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DoubleB_2",
                                "DoubleMu2012C_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DoubleC_2",
                                "DoubleMu2012D_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DoubleD_2",
                                "DoubleEle2012A_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DoubleA_2",
                                "DoubleEle2012B_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DoubleB_2",
                                "DoubleEle2012C_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DoubleC_2",
                                "DoubleEle2012D_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DoubleD_2",
                                "DYjets_Pt50to70_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DYPt50_70_2",
                                "DYjets_Pt70to100_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DYPt70_100_2",
                                "DYjets_Pt100_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DYPt100_2",
                                "DYjets_Pt180_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DYPt180_2",
                                "DYjets_M10to50_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DYM10_50_2",
                                "ZZ_Summer12_final_skimed_llbbX.root":"ReReco_llbb_ZZ_2",
                                "TTFullLept_Summer12_final_skimed_llbbX.root":"ReReco_llbb_TTFull_All_2",
				"TTSemiLept_Summer12_final_skimed_llbbX.root":"ReReco_llbb_TTSemi_2",
                                "ZH125_Summer12_final_skimed_llbbX.root":"ReReco_llbb_ZH125_2",
                                "DYjets_HT200to400_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DYHT200_2",
				"DYjets_HT400_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DYHT400_2",
				"WZ_Summer12_final_skimed_llbbX.root":"ReReco_llbb_WZ_2",
				"WW_Summer12_final_skimed_llbbX.root":"ReReco_llbb_WW_2",
				"Wt_Summer12_final_skimed_llbbX.root":"ReReco_llbb_Wt_2",
				"DYinc_Summer12_final_skimed_llbbX.root":"ReReco_llbb_DYinc_2",
				"Wtbar_Summer12_final_skimed_llbbX.root":"ReReco_llbb_Wtbar_2",

			   }

#Do you want to keep events with no weights in the output tree (with value set to -1 so far) or to get rid of them?
keepEventWithNoWeight=True

#What is the maximal number of event with weight you want for each sample (-1 for no threshold)? For instance, TT sample has ~1M llbb event but only 100K weights computed --> avoid loss of time
MaxNumberOfEvt=-1  #100000
keepRooWorkSpace=False
#label="NoRWS_V0"
label="V3"
for sample in dict_Sample_nameInInstance :
	inRootFile = directory+sample
	inRootFileBDT=inRootFile.replace(".root","_withWeights_V3.root")
	inRootFileBDT_RWS=inRootFile.replace(".root","_withWeights_V3_BDT.root")	
	mergeWeightsInRootFile_loopOnTree_NoLoopOnWeightFile(inRootFile,dict_Sample_nameInInstance[sample],stages,dict_InstanceNameInTree_ChannelNames, MW_directory, stringsToLookFor,keepEventWithNoWeight,MaxNumberOfEvt,keepRooWorkSpace,label)
        mergeBDT_NN(inRootFileBDT,stages)
	
	
        #addWorkspace(inRootFileBDT_RWS)


	#dict_hypoName_filewith_weights={hypo : MW_directory+hypo+"/Events/"+dict_DataSample_hypo_nameInHypo[DataSample][hypo]+"/"+nameOfweightsFile for hypo in dict_DataSample_hypo_nameInHypo[DataSample]}
	#for hypo in dict_DataSample_hypo_nameInHypo[DataSample] : 
		#file_list_with_weights.append(MW_directory+hypo+"/"+dict_DataSample_hypo_nameInHypo[DataSample][hypo]+"/"+nameOfweightsFile)
	#print "Weights to be merged : ", file_list_with_weights
	#mergeWeightsInRootFile(inRootFile, file_list_with_weights, stringsToLookFor)
        #print "Weights to be merged : "
        #print dict_InstanceNameInTree_ChannelNames[sample].keys() 

	
