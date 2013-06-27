from ROOT import *

i=1

DYMC_mu = "Mu_MC"

file ={}
ws   ={}
myRDS={}

file[i]  = TFile("File_rds_zbb_"+DYMC_mu+"_slice"+str(i)+".root")
ws[i]    = file[i].Get("ws")
myRDS[i] = ws[i].data("rds_zbb")

print "myRDS[", i ,"].numEntries() = ", myRDS[i].numEntries()

for i in range(2,21):
    file[i]  = TFile("File_rds_zbb_"+DYMC_mu+"_slice"+str(i)+".root")
    ws[i]    = file[i].Get("ws")
    myRDS[i] = ws[i].data("rds_zbb")
    myRDS[1].append(myRDS[i])
    print "myRDS[", i ,"].numEntries() = ", myRDS[i].numEntries()

print "***"
print "final dataset myRDS[", 1 ,"].numEntries() = ", myRDS[1].numEntries()


sumws = RooWorkspace("ws","workspace")
getattr(sumws,'import')(myRDS[1])
sumws.Print()

sumws.writeToFile("File_rds_zbb_"+DYMC_mu+".root")
gDirectory.Add(sumws)
                
