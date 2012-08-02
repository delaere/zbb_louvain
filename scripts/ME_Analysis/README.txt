***********************************************************
***********************************************************


			MW Analysis


***********************************************************
***********************************************************

In inputFiles:
You must copy in this directory the lhco file and lhco converted to root file and the event info rootfile.
This directory will also contains the output of the MW_Analysis (which are input for the NN estimation code)

***********************************************************\

In MW_Analysis:

1. Untar and install ExRootAnalysis

Code and script content :
1. "MW_analysis_All_Full_v4.C" called "MW_Analysis" code
For each dataset this macro create a tree (tree2) containing the (-log10) of the weight for the following hypothesis : gg, qq, tt, zzC0, zzC3, zhC0, zhC3, twb. 
It contains also information as event and run number.
The macro is submitted with the June_2012.sh script.
Inputs are : location of the weights for all the hypothesis, lhco event file converted in root and the event info file provided at the same time as the rootfile.
The output is a root file with the tree2.
The output file is the entry of the NN code. It is also the file which must be merged at RDS level.

2. "June_2012.sh"
script bash to submit the MW_Analysis.
PATH of the MadWeight output file for each instance must be specified.
PATH of the location of the lhco and event info file is specified.

3. "include.h"
avoid to put all include line in each file


***********************************************************\

In MW_Analysis/NN_AN:\

1. "Generic_NN.C"
macro to train NN to distinguish signal and background. 
To be use it for the Zbb Analysis (ZH analysis).
Inputs are the output of "MW_Analysis" code for each dataset (DY,tt,ZZ,ZH,twb,DATA).
Many option must be checked IN THE CODE :
You can specified IN THE CODE if a dataset must be considered as signal/background and if it must be used for the NN training.AS:
	
	Input(dy,N1,var1,sim,simu,XX,YY);

	where XX (0 or 1) say if the dataset will be considered for the NN training.
	where YY (0 or 1) say if it's signal (1) or background (0).
You have to specified the NN struct and the input of the NN:

	TMultiLayerPerceptron *mlp = new TMultiLayerPerceptron("@gg_weight,@qq_weight,@tt_weight,@Met:5:type","(type==0)/31029.+(type==1)/824.",simu,"Entry$%2!=0", "Entry$%2==0");

	(exemple for tt VS Zbb with 4 entries, 5 node in one intermediate layer)
Specified also the number of iteration.
the NN will be written both in c++ and in python in the "MW_Analysis/NN/" directory.

By default it's configured for tt VS Zbb.

2. "Generic_NN_higgs_test.C"
As previuos code but configured for a simple ZH VS Zbb analysis.

3. "Read_input.h"
Small function used in the Generic_NN code.

4. "NN_June.sh"
Bash script specifying the option to submit the Generic_NN code.
Argument needed : name of the inputfile for each dataset + name of the outputfile.

5. "plot_NN_Full.C"  
Simple code using the MW_Analysis output and the NN function to get some distribution without any reweighting.


