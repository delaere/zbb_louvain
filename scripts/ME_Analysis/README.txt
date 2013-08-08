***********************************************************
***********************************************************


			MW Analysis


***********************************************************
***********************************************************

To start :
You should produce the RooDataSet (if not yet existing) corresponding the samples you are interested to run on.
For this, please refer to the python directory (makeRDS_usingFramework.py)

***********************************************************\

Creating the LHCO files :
1. cd Merging

2. open "createTree1.C"
   - change the input and output folders, if needed. The input files are the RDS produced before and the ouput is the LHCO files + a root files (tree1)
   - add to the function Loop() a line for each samples

3. root -l 
   - .L createTree1.C+
   - Loop()

Compute the weights for each events and hypothesis with MadWeight (see more about this at https://cp3.irmp.ucl.ac.be/projects/cp3admin/wiki/UsersPage/Physics/Exp/HbbwithMEM)

Creating a tree with the weights
1. cd MW_Analysis

2. Untar and install ExRootAnalysis

3. produce the LHCO.root from the LHCO files
   - cd ExRootAnalysis
   - ./ExRootLHCOlympicsConverter myfile.lhco myfile_LHCO.root
(this part will probably be replaced soon to avoid this convertion which could take hours for DATA)

Code and script content :
1. "MW_analysis.C"
For each dataset this macro create a tree (tree2) containing the (-log10) of the weight for the following hypothesis : gg, qq, tt, zzC0, zzC3, zhC0, zhC3, twb. 
It contains also information as event and run number.
The macro is submitted with the "produceTree2.py" script.
Inputs are : location of the weights for all the hypothesis, lhco event file converted in root and the event info file provided at the same time as the rootfile.
The output is a root file with the tree2.
The output file is the entry of the NN code. It is also the file which must be merged at RDS level.

2. "produceTree2.py"
python script to submit the MW_Analysis using 2 bash scripts (Combination_mumu_CSV_2012.sh  Combination_ee_CSV_2012.sh).
different options could be specified in the file

3. "include.h"
avoid to put all include line in each file


***********************************************************\

In MW_Analysis/NN_AN:

1. "Generic_NN.C"
macro to train NN/BDT to distinguish signal and background. 
Inputs are the output of "MW_Analysis" code for each dataset (DY,tt,ZZ,ZH).

2. "Read_input.h"
Small function used in the Generic_NN code.

3. "NN_June.sh"
Bash script specifying the option to submit the Generic_NN code.
Argument needed : name of the inputfile for each dataset + name of the outputfile.

4. "condor.cmd"
to submit NN on condor

5. "doNorm.py"
to normalize the output to compute limits

6. "CSV_nosys.txt"
to compute the limits for the NN output

7. "ComputeGraphFromTrainTxt.C"
make learning curve plots for the TMLP