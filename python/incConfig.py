
from incConfig_data import *

#add to the data configuration the MC ones
updateConfMC(c=configuration)

# fine-tuning of the event content for display
eventDumpConfig.collectionsToHide.append("genParticles")

class configuration(configuration):
    # my variables: files, systematics and other options
    JERfactor = 1.
    JESfactor = 0.
    LeptonTnPfactor = 0 # Lepton reweighting uncertainty
    SF_uncert="mean" #btagging reweighting:  choose among min/max/mean 
