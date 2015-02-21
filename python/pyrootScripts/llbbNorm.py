import os, sys
lib_path = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/storm-0.20-py2.7-linux-x86_64.egg/')
lib_path2 = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/MySQL_python-1.2.3-py2.7-linux-x86_64.egg')
lib_path3 = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg/')
sys.path.append(lib_path)
sys.path.append(lib_path2)
sys.path.append(lib_path3)
from UserCode.zbb_louvain.zbbSamples import *

totDYev = 46515036.

lumi = {
    "DATA"   : 19.7,
    "TTFullLept" : getSample(name="TTFullLept_2014").nevents_processed/getSample(name="TTFullLept_2014").source_dataset.xsection/1000.,
    "TTSemiLept" : getSample(name="TTSemiLept_2014").nevents_processed/getSample(name="TTSemiLept_2014").source_dataset.xsection/1000.,
    "Zbb"     : totDYev/getSample(name="DY_2014").source_dataset.xsection/1000.,
    "Zbx"     : totDYev/getSample(name="DY_2014").source_dataset.xsection/1000.,
    "Zxx"     : totDYev/getSample(name="DY_2014").source_dataset.xsection/1000.,
    "ZZ"     : getSample(name="ZZ_2014").nevents_processed/getSample(name="ZZ_2014").source_dataset.xsection/1000.,
    "WZ"     : getSample(name="WZ_2014").nevents_processed/(getSample(name="WZ_2014").source_dataset.xsection*1.12)/1000.,
    "WW"     : getSample(name="WW_2014").nevents_processed/(getSample(name="WW_2014").source_dataset.xsection*1.22)/1000.,
    "Wt"     : getSample(name="Wt_2014").nevents_processed/(getSample(name="Wt_2014").source_dataset.xsection*1.05)/1000.,
    "Wtbar"  : getSample(name="Wtbar_2014").nevents_processed/(getSample(name="Wtbar_2014").source_dataset.xsection*1.05)/1000.,
    "ZH125"  : getSample(name="ZH125_2014").nevents_processed/getSample(name="ZH125_2014").source_dataset.xsection/1000.,
    "ZA_350_70"  : 25000./0.02/1000.,
    }
