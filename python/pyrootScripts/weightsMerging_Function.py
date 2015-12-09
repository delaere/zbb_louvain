import array
from array import array
from math import log10
from ROOT import *
import ROOT
RooAbsData.setDefaultStorageType(RooAbsData.Tree)
#from ROOT import TFile, TTree, gDirectory


def addWorkspace(inRootFile):
        fileIn = TFile.Open(inRootFile,"read")	
        outRootFile = inRootFile.replace(".root","_RWS.root")
	fileOut = TFile.Open(outRootFile,"recreate")
	
	ws_zbb = fileIn.Get("workspace_ras") # get the RooArgSet from the file
	myRDSRAS = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats()) # define a new RooArgSet using the one you got from the file
	
        
	WZH3 = RooRealVar("MinusLogW_ZH_cor3", "MinusLogW_ZH_cor3", -2, 65)
	WZH0 = RooRealVar("MinusLogW_ZH_cor0", "MinusLogW_ZH_cor0", -2, 65)
	WZZ3 = RooRealVar("MinusLogW_ZZ_cor3", "MinusLogW_ZZ_cor3", -2, 65)
	WZZ0 = RooRealVar("MinusLogW_ZZ_cor0", "MinusLogW_ZZ_cor0", -2, 65)
	WGG = RooRealVar("MinusLogW_gg_Zbb", "MinusLogW_gg_Zbb", -2, 65)
	WQQ = RooRealVar("MinusLogW_qq_Zbb", "MinusLogW_qq_Zbb", -2, 65)	 
	WTT = RooRealVar("MinusLogW_TT", "MinusLogW_TT", -2, 65) 
	BDToutMLPTTDY_Mu_noCat = RooRealVar("bdtOutputMLPTTDY_Mu_noCat", "bdtOutputMLPTTDY_Mu_noCat", -0.4, 1.4) 
	BDToutMLPTTDY_El_noCat = RooRealVar("bdtOutputMLPTTDY_El_noCat", "bdtOutputMLPTTDY_El_noCat", -0.4, 1.4)	
#	BDToutTTDY_Mu_2j = RooRealVar("bdtOutputTTDY_Mu_2j", "bdtOutputTTDY_Mu_2j", -2, 2) 
#	BDToutTTDY_El_2j = RooRealVar("bdtOutputTTDY_El_2j", "bdtOutputTTDY_El_2j", -2, 2) 
#	BDToutTTDY_Mu_3j = RooRealVar("bdtOutputTTDY_Mu_3j", "bdtOutputTTDY_Mu_3j", -2, 2) 
#	BDToutTTDY_El_3j = RooRealVar("bdtOutputTTDY_El_3j", "bdtOutputTTDY_El_3j", -2, 2) 
	BDToutZHAll_Mu_2j = RooRealVar("bdtOutputZHAll_Mu_2j", "bdtOutputZHAll_Mu_2j", -2, 2) 
	BDToutZHAll_El_2j = RooRealVar("bdtOutputZHAll_El_2j", "bdtOutputZHAll_El_2j", -2, 2) 
	BDToutZHAll_Mu_3j = RooRealVar("bdtOutputZHAll_Mu_3j", "bdtOutputZHAll_Mu_3j", -2, 2) 
	BDToutZHAll_El_3j = RooRealVar("bdtOutputZHAll_El_3j", "bdtOutputZHAll_El_3j", -2, 2) 	
	
       
	myRDSRAS.add(WZH3) 
        myRDSRAS.add(WZH0)
	myRDSRAS.add(WZZ3)        
	myRDSRAS.add(WZZ0)
	myRDSRAS.add(WGG)
	myRDSRAS.add(WQQ)
	myRDSRAS.add(WTT)    
	myRDSRAS.add(BDToutZHAll_Mu_3j)
	myRDSRAS.add(BDToutZHAll_El_3j)
	myRDSRAS.add(BDToutZHAll_Mu_2j)
	myRDSRAS.add(BDToutZHAll_El_2j)	
#	myRDSRAS.add(BDToutTTDY_Mu_3j)
#	myRDSRAS.add(BDToutTTDY_El_3j)
#	myRDSRAS.add(BDToutTTDY_Mu_2j)
#	myRDSRAS.add(BDToutTTDY_El_2j)	
	myRDSRAS.add(BDToutMLPTTDY_Mu_noCat)
	myRDSRAS.add(BDToutMLPTTDY_El_noCat)	
			
        t = fileIn.Get("rds_zbb")# it is the tree with the new variables

        myRDS_sum = RooDataSet("rds_zbb", "rds_zbb",t , myRDSRAS)
	
	ras_zbb = myRDS_sum.get() # get the RooArgSet 
	ws_ras = RooWorkspace("workspace_ras","workspace_ras")
	getattr(ws_ras,'import')(ras_zbb)
	ws_ras.writeToFile(outRootFile)
	gDirectory.Add(ws_ras)
	#file_in = TFile.Open(inRootFile,"read")
	fout = TFile.Open(outRootFile,"update")

	
	tree_zbb = myRDS_sum.tree() # get the tree from the RDS
	tree_zbb.Write()
	
	fout.Close()
		
	
def mergeBDT_NN(inRootFile,stages):
        fileIn = TFile.Open(inRootFile,"read")
	print "################################################################\n"
	print "Treating ", inRootFile+"...\n"
	outRootFile = inRootFile.replace(".root","_BDT.root")	
	
#	file_in = ROOT.TFile(inRootFile,"read")
#	file_withWSout = ROOT.TFile(outRootFile,"recreate")
#	ws_ras = file_in.Get("workspace_ras")
#	ws_ras.writeToFile(outRootFile)
#	gDirectory.Add(ws_ras)
#	file_in = TFile.Open(inRootFile,"read")
#	file_withWSout = TFile.Open(outRootFile,"update")
	
	
	fileOut = TFile.Open(outRootFile,"recreate")
	treeIn = fileIn.Get("rds_zbb")
	
	#fileOut = TFile.Open(outRootFile,"recreate")
	treeOut = treeIn.CloneTree(0)
	MLPTTDY_Mu_noCat= array('f',[0])
	MLPTTDY_El_noCat= array('f',[0])  
	bdtTTDY_Mu_noCat= array('f',[0])
	bdtTTDY_El_noCat= array('f',[0]) 	     
	bdtOutputZHAll_Mu_2j= array('f',[0])
	bdtOutputZHAll_El_2j= array('f',[0])
	bdtOutputZHAll_Mu_3j= array('f',[0])
	bdtOutputZHAll_El_3j= array('f',[0])
		
	branch_BDTZHAll_Mu_3j = treeOut.Branch("bdtOutputZHAll_Mu_3j",bdtOutputZHAll_Mu_3j,"bdtOutputZHAll_Mu_3j/F")
	branch_BDTZHAll_El_3j = treeOut.Branch("bdtOutputZHAll_El_3j",bdtOutputZHAll_El_3j,"bdtOutputZHAll_El_3j/F")
	branch_BDTZHAll_Mu_2j = treeOut.Branch("bdtOutputZHAll_Mu_2j",bdtOutputZHAll_Mu_2j,"bdtOutputZHAll_Mu_2j/F")
	branch_BDTZHAll_El_2j = treeOut.Branch("bdtOutputZHAll_El_2j",bdtOutputZHAll_El_2j,"bdtOutputZHAll_El_2j/F")
	branch_MLPTTDY_Mu_noCat = treeOut.Branch("MLPTTDY_Mu_noCat",MLPTTDY_Mu_noCat,"MLPTTDY_Mu_noCat/F")
	branch_MLPTTDY_El_noCat = treeOut.Branch("MLPTTDY_El_noCat",MLPTTDY_El_noCat,"MLPTTDY_El_noCat/F")
	branch_BDTTTDY_Mu_noCat = treeOut.Branch("bdtTTDY_Mu_noCat",bdtTTDY_Mu_noCat,"bdtTTDY_Mu_noCat/F")
	branch_BDTTTDY_El_noCat = treeOut.Branch("bdtTTDY_El_noCat",bdtTTDY_El_noCat,"bdtTTDY_El_noCat/F")

		
	print "Load BDT entries "
	readerMLPTTDY_El_noCat = ROOT.TMVA.Reader()
	readerMLPTTDY_Mu_noCat = ROOT.TMVA.Reader()
	readerBDTTTDY_El_noCat = ROOT.TMVA.Reader()
	readerBDTTTDY_Mu_noCat = ROOT.TMVA.Reader()	
		
	readerZHAll_Mu_2j = ROOT.TMVA.Reader()
	readerZHAll_Mu_3j = ROOT.TMVA.Reader()   
	readerZHAll_El_2j = ROOT.TMVA.Reader()
	readerZHAll_El_3j = ROOT.TMVA.Reader()	    
	
	
	MinusLogW_ZH_cor3 = array('f',[0])  
	MinusLogW_ZH_cor0 = array('f',[0])  
	MinusLogW_ZZ_cor3 = array('f',[0])  
	MinusLogW_ZZ_cor0 = array('f',[0])  
	MinusLogW_TT = array('f',[0])       
	MinusLogW_gg_Zbb = array('f',[0])   
	MinusLogW_qq_Zbb = array('f',[0])   
	
	readerZHAll_Mu_2j.AddVariable("MinusLogW_ZH_cor3",MinusLogW_ZH_cor3)
	readerZHAll_Mu_2j.AddVariable("MinusLogW_ZH_cor0",MinusLogW_ZH_cor0)
	readerZHAll_Mu_2j.AddVariable("MinusLogW_ZZ_cor3",MinusLogW_ZZ_cor3)
	readerZHAll_Mu_2j.AddVariable("MinusLogW_ZZ_cor0",MinusLogW_ZZ_cor0)
	readerZHAll_Mu_2j.AddVariable("MinusLogW_TT",MinusLogW_TT)  
	readerZHAll_Mu_2j.AddVariable("MinusLogW_gg_Zbb",MinusLogW_gg_Zbb)  
	readerZHAll_Mu_2j.AddVariable("MinusLogW_qq_Zbb",MinusLogW_qq_Zbb) 
	 
	
	readerZHAll_Mu_3j.AddVariable("MinusLogW_ZH_cor3",MinusLogW_ZH_cor3)
	readerZHAll_Mu_3j.AddVariable("MinusLogW_ZH_cor0",MinusLogW_ZH_cor0)
	readerZHAll_Mu_3j.AddVariable("MinusLogW_ZZ_cor3",MinusLogW_ZZ_cor3)
	readerZHAll_Mu_3j.AddVariable("MinusLogW_ZZ_cor0",MinusLogW_ZZ_cor0)
	readerZHAll_Mu_3j.AddVariable("MinusLogW_TT",MinusLogW_TT)  
	readerZHAll_Mu_3j.AddVariable("MinusLogW_gg_Zbb",MinusLogW_gg_Zbb)  
	readerZHAll_Mu_3j.AddVariable("MinusLogW_qq_Zbb",MinusLogW_qq_Zbb)  
	
	readerZHAll_El_3j.AddVariable("MinusLogW_ZH_cor3",MinusLogW_ZH_cor3)
	readerZHAll_El_3j.AddVariable("MinusLogW_ZH_cor0",MinusLogW_ZH_cor0)
	readerZHAll_El_3j.AddVariable("MinusLogW_ZZ_cor3",MinusLogW_ZZ_cor3)
	readerZHAll_El_3j.AddVariable("MinusLogW_ZZ_cor0",MinusLogW_ZZ_cor0)
	readerZHAll_El_3j.AddVariable("MinusLogW_TT",MinusLogW_TT)  
	readerZHAll_El_3j.AddVariable("MinusLogW_gg_Zbb",MinusLogW_gg_Zbb)  
	readerZHAll_El_3j.AddVariable("MinusLogW_qq_Zbb",MinusLogW_qq_Zbb) 	
	
	readerZHAll_El_2j.AddVariable("MinusLogW_ZH_cor3",MinusLogW_ZH_cor3)
	readerZHAll_El_2j.AddVariable("MinusLogW_ZH_cor0",MinusLogW_ZH_cor0)
	readerZHAll_El_2j.AddVariable("MinusLogW_ZZ_cor3",MinusLogW_ZZ_cor3)
	readerZHAll_El_2j.AddVariable("MinusLogW_ZZ_cor0",MinusLogW_ZZ_cor0)
	readerZHAll_El_2j.AddVariable("MinusLogW_TT",MinusLogW_TT)  
	readerZHAll_El_2j.AddVariable("MinusLogW_gg_Zbb",MinusLogW_gg_Zbb)  
	readerZHAll_El_2j.AddVariable("MinusLogW_qq_Zbb",MinusLogW_qq_Zbb)  
	
	
	readerBDTTTDY_Mu_noCat.AddVariable("MinusLogW_TT",MinusLogW_TT)  
	readerBDTTTDY_Mu_noCat.AddVariable("MinusLogW_gg_Zbb",MinusLogW_gg_Zbb)  
	readerBDTTTDY_Mu_noCat.AddVariable("MinusLogW_qq_Zbb",MinusLogW_qq_Zbb)
	
	readerBDTTTDY_El_noCat.AddVariable("MinusLogW_TT",MinusLogW_TT)  
	readerBDTTTDY_El_noCat.AddVariable("MinusLogW_gg_Zbb",MinusLogW_gg_Zbb)  
	readerBDTTTDY_El_noCat.AddVariable("MinusLogW_qq_Zbb",MinusLogW_qq_Zbb)	
	
	readerMLPTTDY_Mu_noCat.AddVariable("MinusLogW_TT",MinusLogW_TT)  
	readerMLPTTDY_Mu_noCat.AddVariable("MinusLogW_gg_Zbb",MinusLogW_gg_Zbb)  
	readerMLPTTDY_Mu_noCat.AddVariable("MinusLogW_qq_Zbb",MinusLogW_qq_Zbb)
	
	readerMLPTTDY_El_noCat.AddVariable("MinusLogW_TT",MinusLogW_TT)  
	readerMLPTTDY_El_noCat.AddVariable("MinusLogW_gg_Zbb",MinusLogW_gg_Zbb)  
	readerMLPTTDY_El_noCat.AddVariable("MinusLogW_qq_Zbb",MinusLogW_qq_Zbb)	
	
	readerBDTTTDY_Mu_noCat.BookMVA("BDT","weights/BDT_NN_trainningTTvsDY_Mu_noCat_BDT.weights.xml")
	readerBDTTTDY_El_noCat.BookMVA("BDT","weights/BDT_NN_trainningTTvsDY_El_noCat_BDT.weights.xml")	
	readerMLPTTDY_Mu_noCat.BookMVA("MLP","weights/BDT_NN_trainningTTvsDY_Mu_noCat_MLP.weights.xml")
	readerMLPTTDY_El_noCat.BookMVA("MLP","weights/BDT_NN_trainningTTvsDY_El_noCat_MLP.weights.xml")		
	
	
	readerZHAll_Mu_2j.BookMVA("BDT","weights/BDT_NN_trainningZHvsOther_Mu_2j_BDT.weights.xml")
	readerZHAll_El_2j.BookMVA("BDT","weights/BDT_NN_trainningZHvsOther_El_2j_BDT.weights.xml")
	readerZHAll_Mu_3j.BookMVA("BDT","weights/BDT_NN_trainningZHvsOther_Mu_3j_BDT.weights.xml")
	readerZHAll_El_3j.BookMVA("BDT","weights/BDT_NN_trainningZHvsOther_El_3j_BDT.weights.xml")	
	
        for entry in xrange(treeIn.GetEntries()):
		treeIn.GetEntry(entry)
		
		MinusLogW_ZH_cor0[0]=float(treeIn.MinusLogW_ZH_cor0)
		MinusLogW_ZH_cor3[0]=float(treeIn.MinusLogW_ZH_cor3)
		MinusLogW_ZZ_cor3[0]=float(treeIn.MinusLogW_ZZ_cor3)
		MinusLogW_ZZ_cor0[0]=float(treeIn.MinusLogW_ZZ_cor0)
		MinusLogW_gg_Zbb[0]=float(treeIn.MinusLogW_gg_Zbb)
		MinusLogW_qq_Zbb[0]=float(treeIn.MinusLogW_qq_Zbb)
		MinusLogW_TT[0]=float(treeIn.MinusLogW_TT)
		bdtTTDY_El_noCat[0] = 0.5;
		bdtTTDY_Mu_noCat[0] = 0.5;
		MLPTTDY_El_noCat[0] = 0.5;
		MLPTTDY_Mu_noCat[0] = 0.5;	       
		
		bdtOutputZHAll_El_3j[0] =0.5;
		bdtOutputZHAll_Mu_3j[0] =0.5;
		bdtOutputZHAll_El_2j[0] =0.5;
		bdtOutputZHAll_Mu_2j[0] =0.5;		
		for stage in stages:
			if getattr(treeIn,stage) :
			  if (MinusLogW_gg_Zbb[0]> 2 and MinusLogW_gg_Zbb[0]<50 ) and (MinusLogW_qq_Zbb[0]> 2 and MinusLogW_qq_Zbb[0]<50 ) and (MinusLogW_TT[0]> 2 and MinusLogW_TT[0]<50 ):

			     if "rc_stage_6_idx" in stage:
			         MLPTTDY_Mu_noCat[0] = readerMLPTTDY_Mu_noCat.EvaluateMVA("MLP")
			         bdtTTDY_Mu_noCat[0] = readerBDTTTDY_Mu_noCat.EvaluateMVA("BDT")			    
			     if "rc_stage_16_idx" in stage:
			         MLPTTDY_El_noCat[0] = readerMLPTTDY_El_noCat.EvaluateMVA("MLP")
			         bdtTTDY_El_noCat[0] = readerBDTTTDY_El_noCat.EvaluateMVA("BDT")
			     	
			     if (MinusLogW_ZH_cor0[0]> 2 and MinusLogW_ZH_cor0[0]<50 ) and (MinusLogW_ZH_cor3[0]> 2 and MinusLogW_ZH_cor3[0]<50 ) and (MinusLogW_ZZ_cor3[0]> 2 and MinusLogW_ZZ_cor3[0]<50 ) and (MinusLogW_ZZ_cor0[0]> 2 and MinusLogW_ZZ_cor0[0]<50 ):		   
			        if "rc_stage_6_idx" in stages:
			            bdtOutputZHAll_Mu_3j[0] = readerZHAll_Mu_3j.EvaluateMVA("BDT")
			            bdtOutputZHAll_Mu_2j[0] = readerZHAll_Mu_2j.EvaluateMVA("BDT")				   
			        elif "rc_stage_6_idx" in stages:
			            bdtOutputZHAll_El_3j[0] = readerZHAll_El_3j.EvaluateMVA("BDT")
			            bdtOutputZHAll_El_2j[0] = readerZHAll_El_2j.EvaluateMVA("BDT")
			  
	        treeOut.Fill()
	        	
	treeOut.Write()
	#file_withWSout.Close()
	fileOut.Close()
	print outRootFile, "written.\n"
	fileIn.Close()		
  

def mergeWeightsInRootFile_loopOnTree_NoLoopOnWeightFile(inRootFile,nameInInstance,stages,dict_InstanceNameInTree_ChannelNames, MW_directory, stringToLookFor,keepEventWithNoWeight,MaxNumberOfEvt,keepRooWorkSpace,label):
	fileIn = TFile.Open(inRootFile,"read")
	print "################################################################\n"
	print "Treating ", inRootFile+"...\n"
	print "Keep the rooWorkSpace? :", keepRooWorkSpace
	treeIn = fileIn.Get("rds_zbb")
	outRootFile = inRootFile.replace(".root","_withWeights_"+label+".root")
	fileOut = TFile.Open(outRootFile,"recreate")		

        if keepRooWorkSpace :
		ws_ras = fileIn.Get("workspace_ras")
		ws_ras.writeToFile(outRootFile)
		gDirectory.Add(ws_ras)
		fileIn = TFile.Open(inRootFile,"read")
		fileOut = TFile.Open(outRootFile,"update")		

	
	#dict_nameHypo_stages_weightsFile = {nameHypo : {stages[i] : MW_directory+dict_InstanceNameInTree_ChannelNames[nameHypo][i]+"/Events/"+nameInInstance+"/weights.out" for i in xrange(len(stages))} for nameHypo in dict_InstanceNameInTree_ChannelNames}
	dict_nameHypo_stages_weightsFile = {}
	for nameHype in dict_InstanceNameInTree_ChannelNames :
		val = {}
		for i in xrange(len(stages)) :
			val[ stages[i] ] = MW_directory+dict_InstanceNameInTree_ChannelNames[nameHypo][i]+"/Events/"+nameInInstance+"/weights.out"
		dict_nameHypo_stages_weightsFile[ nameHypo ] = val

        print "Weight file to merge : "
	print dict_nameHypo_stages_weightsFile,"\n"
	hasAllWeightsArray =  array("d",[0])
	treeOut = treeIn.CloneTree(0)
	branch_hasAllWeightsArray_newTree=treeOut.Branch("hasAllWeights",hasAllWeightsArray,"hasAllWeights")
	#weightsArray = {hypo : array("d",[0]) for hypo in dict_InstanceNameInTree_ChannelNames}
	weightsArray = {}
	for hypo in dict_InstanceNameInTree_ChannelNames:
		weightsArray[hypo] = array("d",[0])
	#weightsErrorArray = {hypo : array("d",[0]) for hypo in dict_InstanceNameInTree_ChannelNames}
	weightsErrorArray = {}
	for hypo in dict_InstanceNameInTree_ChannelNames:
		weightsErrorArray[hypo] = array("d",[0])
	#minusLogWeightsArray = {hypo : array("d",[0]) for hypo in dict_InstanceNameInTree_ChannelNames}
        minusLogWeightsArray = {}
	for hypo in dict_InstanceNameInTree_ChannelNames:
		minusLogWeightsArray = array("d",[0])

        #dict_hypo_stage_evtRunNum_weightErr = {nameHypo : {stages[i] :{} for i in xrange(len(stages))} for nameHypo in dict_InstanceNameInTree_ChannelNames} 
	dict_hypo_stage_evtRunNum_weightErr = {}
	for nameHypo in dict_InstanceNameInTree_ChannelNames:
		val = {}
		for i in xrange(len(stages)):
			val [stages[i]] = {}
		dict_hypo_stage_evtRunNum_weightErr[nameHypo] = val
	print "Start to put the weights into python dictionnaries to avoid loops for each event.\n"
	for hypo in dict_InstanceNameInTree_ChannelNames :
		leave_weight = hypo+"/D" 
		branch_weight_newTree = treeOut.Branch("W_"+hypo,weightsArray[hypo],"W_"+hypo)
		branch_weightError_newTree = treeOut.Branch("W_"+hypo+"_error",weightsErrorArray[hypo],"W_"+hypo+"_error/D")
		branch_minusLogweight_newTree = treeOut.Branch("MinusLogW_"+hypo,minusLogWeightsArray[hypo],"MinusLogW_"+hypo+"/D")
		for stage in stages : 
			weightFile=dict_nameHypo_stages_weightsFile[hypo][stage]
                        try: file=open(weightFile,'r')
                        except IOError :
                        	print "Instance ", weightFile, " does not exist. Weights may be set to -1.\n"
				continue
			lines=file.read().split("\n")
			table_evtRun=[]
			table_weights=[]
			table_errorWeights=[]
			dict_evtRun_poidErr = {}
			for line in lines :
				if stringToLookFor in line :
					pieces=line.split('@')
					eventNumber=int(pieces[0])
					lastpieces=pieces[1].split(" ")
					for charIndex in xrange(len(lastpieces[0])):
						try : int(lastpieces[0][charIndex])
						except ValueError : continue
						runNumber=lastpieces[0][charIndex:]
						break
					eventWeight=float(lastpieces[-3])
                                        eventWeightError=float(lastpieces[-2])
					table_evtRun.append(pieces[0]+runNumber)
					table_weights.append(eventWeight)
					table_errorWeights.append(eventWeightError)
			tmpmap = {}
			for index in xrange(len(table_evtRun)):
				tmpmap [table_evtRun[index]] = [table_weights[index],table_errorWeights[index]]
			#dict_hypo_stage_evtRunNum_weightErr[hypo][stage]={table_evtRun[index]:[table_weights[index],table_errorWeights[index]] for index in xrange(len(table_evtRun))}
			dict_hypo_stage_evtRunNum_weightErr[hypo][stage]=tmpmap

	NevtWithWeight=0	
	print "Starting the loop on the tree.\n"	
	for entry in xrange(treeIn.GetEntries()):
	        if(NevtWithWeight>=MaxNumberOfEvt and not MaxNumberOfEvt==-1): break
		for hypo in dict_nameHypo_stages_weightsFile :
			weightsArray[hypo][0]=-1
                	weightsErrorArray[hypo][0]=-1
			minusLogWeightsArray[hypo][0]=-1
		hasAllWeightsArray[0] = 1 
		treeIn.GetEntry(entry)
		event=int(treeIn.eventSelectionevent)
		run=int(treeIn.eventSelectionrun)
		isInatLeastOneStage=0
		for stage in stages:
			if getattr(treeIn,stage) :
				isInatLeastOneStage=1
				for hypo in dict_nameHypo_stages_weightsFile :
					evtRun = str(event)+str(run)
					try : 
						eventWeight=dict_hypo_stage_evtRunNum_weightErr[hypo][stage][evtRun][0]
						eventWeightError=dict_hypo_stage_evtRunNum_weightErr[hypo][stage][evtRun][1]
						hasWeight=True
						weightsArray[hypo][0]= eventWeight if eventWeight!=0 else 1e-60
						weightsErrorArray[hypo][0]= eventWeightError if eventWeight!=0 else 0
						minusLogWeightsArray[hypo][0]= -log10(weightsArray[hypo][0])

					except KeyError : 
						hasAllWeightsArray[0] = 0
						
		
		if keepEventWithNoWeight or (hasAllWeightsArray[0] == 1 and isInatLeastOneStage) : 
			NevtWithWeight+=1
			treeOut.Fill()	
	treeOut.Write()
	fileOut.Close()
	print "Number of kept events : ", NevtWithWeight
	print outRootFile, "written.\n"
	fileIn.Close()
	
