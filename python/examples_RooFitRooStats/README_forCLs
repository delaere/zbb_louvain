###############################################################################
#                                                                             #
# Documentation of official CMS search code:                                  #
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideHiggsAnalysisCombinedLimit  #
#                                                                             #  
# The code below is based on                                                  #
# CMSSW_5_2_0/src/HiggsAnalysis/CombinedLimit/data/benchmarks/shapes          #
#                                                                             #  
###############################################################################

- Step 0)
To make the CLs one needs 
CMSSW_5_2_0/src/HiggsAnalysis/CombinedLimit
First get this code
Example:
* cmsrel CMSSW_5_2_0
* cmsenv
* cvs co HiggsAnalysis/CombinedLimit

- Step 1) 
Update TH1shapes.root,
using the code as available in UserCode/zbb_louvain/python. 
Running this script will produce the root-file with TH1s in the correct format for the CMS search code:

* /UserCode/zbb_louvain/python/selectionCuts_fromRDS.py

(Based on /UserCode/zbb_louvain/python/getYields_fromRDS.py. To do: merge these scripts.)

- Step 2)
Make limits and combine ouput

combine -M Asymptotic search-ZHbb-115.txt -m 115
combine -M Asymptotic search-ZHbb-120.txt -m 120
combine -M Asymptotic search-ZHbb-125.txt -m 125
combine -M Asymptotic search-ZHbb-130.txt -m 130
combine -M Asymptotic search-ZHbb-135.txt -m 135

hadd -f higgsCombineTest.Asymptotic.root higgsCombineTest.Asymptotic.mH115.root higgsCombineTest.Asymptotic.mH120.root higgsCombineTest.Asymptotic.mH125.root higgsCombineTest.Asymptotic.mH130.root higgsCombineTest.Asymptotic.mH135.root

- Step 3)
Make Brazilian band plot. Run:

python -i makeBrazilianBandPlot.py


