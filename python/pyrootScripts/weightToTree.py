
from ROOT import *
import sys, os
import array

from globalLists import listToProcessEMu, dirTree2_JESup, dirTree2_JESdown, dirTree2

print listToProcessEMu
#list of process hypo.
listHYPO = [
    "ggZbb",
    "qqZbb",
    "ttbar",
    "ZZ_C0",
    "ZZ_C3",
    "ZH_C0",
    "ZH_C3",
    ]

nameHYPO = {
    "ggZbb" : "gg",
    "qqZbb" : "qq",
    "ttbar" : "tt",
    "ZZ_C0" : "zz0",
    "ZZ_C3" : "zz3",
    "ZH_C0" : "hi0",
    "ZH_C3" : "hi3",
    }

#list of param. hypo.
massHYPO = [
    "_110",
    "_115",
    "_120",
    "_125",
    "_130",
    "_135",
    "_140",
    "_145",
    "_150",
    ]

systematics = [
    "",
    #"_JESup",
    #"_JESdown",
    ]
DIR = {
    "" : dirTree2,
    "_JESup": dirTree2_JESup,
    "_JESdown" : dirTree2_JESdown,
    }

HYPO = "ZZ_C3"
channel = "_ee"
syst = "_JESdown"
runName = ""#DY_537"+syst+channel
dir = "/nfs/user/acaudron/Tree2_537"+syst+"/"
filename = "ME_zbb_"+runName.split("_")[0]+channel.replace("mumu","Mu").replace("ee","El")+"_MC.root"


def readWeightFile(HYPO="", channel="", runName=""):
    #open file containing the weights for a given hypo.
    os.system('ls /home/fynu/acaudron/scratch/new_MWjobs/madweight5_interface/'+HYPO+channel+'/Events/'+runName+'/weights.out')
    infile = open('/home/fynu/acaudron/scratch/new_MWjobs/madweight5_interface/'+HYPO+channel+'/Events/'+runName+'/weights.out','r')
    #prepare list of events
    events = []
    #to count number of 0 results
    n0 = 0
    #to count number of param. hypo.
    nHypo = 1
    #loop over the lines
    for line in infile:
        #remove comment line
        if "#" in line : continue
        #get the events splitting the line with the spaces and removing the end line ch.
        event = line.split(" ")[:-1]
        #check that the number of information / line is OK
        if len(event)<4 or len(event)>5 :
            print "Error : event format is not correct, please check the file"
            print "bad event is : ", event
            break
        #check 0 results
        if event[len(event)-2]=="0.0" : n0+=1
        #check the number param. hypo.
        if int(event[len(event)-3])>nHypo : nHypo=int(event[len(event)-3])
        #add the event to the list
        events.append(event)
    #check the length event format
    if len(event)==4 :
        print "event fomat is : event number ; hypo tested ; weight ; weight error"
    else :
        print "event fomat is : run number ; event number ; hypo tested ; weight ; weight error"
    print "number of events processed", len(events)/nHypo
    print "number of 0 results", n0
    print "number of tested hypo", nHypo
    #return the event list + the number of hypothesis
    return (events, nHypo)

def loop(filename="", channel="", runName=""):
    #to retieve all events
    HYPOevents = {}
    #count the number of events
    nevents = 0
    #loop over all process hypo.
    for HYPO in listHYPO:
        #get the events
        HYPOevents[HYPO] = readWeightFile(HYPO=HYPO, channel=channel, runName=runName)
        #check the number of events
        if nevents>0 and nevents!=len(HYPOevents[HYPO][0])/HYPOevents[HYPO][1] :
            print "Error : different number of events processed for the different HYPO"
            print nevents, len(HYPOevents[HYPO][0])/HYPOevents[HYPO][1]
            sys.exit()
        nevents = len(HYPOevents[HYPO][0])/HYPOevents[HYPO][1]
        if HYPOevents[HYPO][1]==1 : continue
        #in case of multiple param. hypo.
        for h in range(1,HYPOevents[HYPO][1]+1) :
            tmp = []
            for event in HYPOevents[HYPO][0] :
                #check if the param. hypo.
                if not int(event[1])==h : continue
                tmp.append(event)
            #append list of events for a param. hypo.
            HYPOevents[HYPO+massHYPO[h-1]]=(tmp,1)
        #remove useless list of events in case of multiple param. hypo.
        del HYPOevents[HYPO]
    print "number hypo. tested is :", len(HYPOevents)

    #define output file, tree and branches
    fileout = TFile(filename,"RECREATE")
    tree2 = TTree("tree2","Weight tree")

    runNumber=array.array("L",[1])
    b0 = tree2.Branch("runNumber",runNumber,"runNumber/l")

    eventNumber=array.array("L",[0])
    b1 = tree2.Branch("eventNumber",eventNumber,"eventNumber/l")

    weight = {}
    b2 = {}
    weightError = {}
    b3 = {}
    for HYPO in HYPOevents :
        if "ZH" in HYPO:
            postfix=nameHYPO[HYPO[:-4]]+HYPO[-4:]
        else :
            postfix=nameHYPO[HYPO]
        weight[HYPO] = array.array("d",[0.])
        b2[HYPO] = tree2.Branch("W"+postfix,weight[HYPO],"W/D")

        weightError[HYPO] = array.array("d",[0.])
        b3[HYPO] = tree2.Branch("Werr"+postfix,weightError[HYPO],"Werr/D")

    #loop over all events to fill the tree
    for i in range(0,nevents):
        #get events
        events = HYPOevents[listHYPO[0]][0]
        #fix run number to one : valid for MC only
        runNumber[0]=1
        #take the evt number
        eventNumber[0]=long(events[i][0])
        #loop over all hypo.
        for HYPO in HYPOevents :
            #get events for HYPO
            events = HYPOevents[HYPO][0]
            #protection against empty list
            if i>=len(events) :
                print "Error : wrong events for HYPO", HYPO
                continue
            #check event number
            if not long(events[i][0])==eventNumber[0] :
                print "Error : not looking to the good event", events[i][0], "instead of", eventNumber[0]
            #fill weights
            weight[HYPO][0]=-log10(float(events[i][2]))
            weightError[HYPO][0]=-log10(float(events[i][3]))
            #replace 0 results by 50.
            if float(events[i][2])==0. :
                weight[HYPO][0]=50.
                weightError[HYPO][0]=50.
        tree2.Fill()
    tree2.Write()
    fileout.Close()

for syst in systematics :
    for proc in listToProcessEMu :
        channel = "_ee"
        if "Mu" in proc : channel = "_mumu"
        runName = proc.split("_")[0]+"_537"+syst+channel
        dir = DIR[syst]
        filename = dir+"ME_zbb_"+runName.split("_")[0]+channel.replace("mumu","Mu").replace("ee","El")+"_MC.root"
        loop(filename=filename,channel=channel,runName=runName)
        print "------------------------------------------------------"
        print "------------------------------------------------------"
        print "                                                      "
        print "------------------------------------------------------"
        print "------------------------------------------------------"
