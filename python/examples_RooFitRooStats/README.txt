###################################################################################################################
#                                                                                                                 #
# Documentation of official CMS search code:                                                                      #
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideHiggsAnalysisCombinedLimit#For_end_users_that_don_t_need_to #  
#                                                                                                                 #
# The code below is based on                                                                                      #
# HiggsAnalysis/CombinedLimit/data/benchmarks/shapes                                                              #
#                                                                                                                 #  
###################################################################################################################

- Step 0)
To make the CLs one needs :
HiggsAnalysis/CombinedLimit (check last cmssw version to use on the twiki
First get this code
Example:
* cmsrel CMSSW_5_2_0
* cmsenv
* cvs co HiggsAnalysis/CombinedLimit (or look to the cms twiki to use GIT)

- Step 1) 
Go to your working CMSSW version
Create myshapes.root (or the name you like) : just a rootfile with a list of histograms (one by process)
 for this you can, for example, use zbb_louvain/python/pyrootScripts/makeCPgetYields_fromRDS.py with theoption goToCLs set at True

- Step 2)
Go to your CMSSW version you setup in 0)
Update your text file with the path to the rootfile previously created (and eventually to the name of the histograms, extension for systematics ...)
Make limits and combine ouput

combine -M Asymptotic search-ZHbb-115.txt -m 115
combine -M Asymptotic search-ZHbb-120.txt -m 120
combine -M Asymptotic search-ZHbb-125.txt -m 125
combine -M Asymptotic search-ZHbb-130.txt -m 130
combine -M Asymptotic search-ZHbb-135.txt -m 135

useful options :
'-t -1' or '--run=blind' : will compute the expected limit ignoring the data
'--run=expected' : will compute the expected only but the data are used
'-S 0' : to ignor systematics (automatically done if no systematics added in the text file)
possible to extract the signal injection also 

In case you want to compute the significance and p-value, you can do :
combine -M ProfileLikelihood --significance datacard.txt -t -1 --expectSignal=1 --toysFreq -m 125

hadd -f higgsCombineTest.Asymptotic.root higgsCombineTest.Asymptotic.mH115.root higgsCombineTest.Asymptotic.mH120.root higgsCombineTest.Asymptotic.mH125.root higgsCombineTest.Asymptotic.mH130.root higgsCombineTest.Asymptotic.mH135.root

- Step 3)
Make Brazilian band plot. Run:

python -i makeBrazilianBandPlot.py


