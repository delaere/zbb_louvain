import os, sys
lib_path = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/storm-0.20-py2.7-linux-x86_64.egg/')
lib_path2 = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/MySQL_python-1.2.3-py2.7-linux-x86_64.egg')
lib_path3 = os.path.abspath('/nfs/soft/python/python-2.7.3-sl5_amd64_gcc41/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg/')
sys.path.append(lib_path)
sys.path.append(lib_path2)
sys.path.append(lib_path3)
from UserCode.zbb_louvain.zbbSamples import *

totDYev = 46515036.
try: 
    lumi = {
        "DATA"   : 19.7,
        "TTFullLept" : getSample(name="TTFullLept_2014").nevents_processed/getSample(name="TTFullLept_2014").source_dataset.xsection/1000.,
        "TTSemiLept" : getSample(name="TTSemiLept_2014").nevents_processed/getSample(name="TTSemiLept_2014").source_dataset.xsection/1000.,
        "Zbb"     : totDYev/getSample(name="DY_2014").source_dataset.xsection/1000.,
        "Zbx"     : totDYev/getSample(name="DY_2014").source_dataset.xsection/1000.,
        "Zxx"     : totDYev/getSample(name="DY_2014").source_dataset.xsection/1000.,
        "DYjets"     : totDYev/getSample(name="DY_2014").source_dataset.xsection/1000.,
        "ZZ"     : getSample(name="ZZ_2014").nevents_processed/getSample(name="ZZ_2014").source_dataset.xsection/1000.,
        "WZ"     : getSample(name="WZ_2014").nevents_processed/(getSample(name="WZ_2014").source_dataset.xsection*1.09)/1000.,
        "WW"     : getSample(name="WW_2014").nevents_processed/(getSample(name="WW_2014").source_dataset.xsection*1.01)/1000.,
        "Wt"     : getSample(name="Wt_2014").nevents_processed/(getSample(name="Wt_2014").source_dataset.xsection*1.05)/1000.,
        "Wtbar"  : getSample(name="Wtbar_2014").nevents_processed/(getSample(name="Wtbar_2014").source_dataset.xsection*1.05)/1000.,
        "ZH125"  : getSample(name="ZH125_2014").nevents_processed/getSample(name="ZH125_2014").source_dataset.xsection/1000.,
        "ZA_350_70"  : 25000./0.02/1000.,
        "ZA_262_99"  : 25000./0.1112/1000,
        "ZA_286_93"  : 25000./0.09419/1000,
        }
except:
    lumi = {'TTSemiLept': 232.73642857142858, 'ZH125': 40139.036144578313, 'WW': 176.81101485148514, 'ZA_286_93': 265.42095763881514, 'ZZ': 1195.1107317073172, 'ZA_262_99': 224.8201438848921, 'Zxx': 13.275937791655132, 'DATA': 19.699999999999999, 'WZ': 273.05272498907817, 'Wtbar': 42.338910338910338, 'Zbb': 13.275937791655132, 'ZA_350_70': 1250.0, 'Wt': 42.699099099099108, 'TTFullLept': 443.9198901098901, 'Zbx': 13.275937791655132}
    print "Warning: database not accessible!"
