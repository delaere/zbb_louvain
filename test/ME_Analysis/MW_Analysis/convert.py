
out = open('Events/DoubleDataA_537_mumu/weight.out','w')

weightout = open('Events/DoubleDataA_537_mumu/DoubleDataA_537_mumu_weights.out','r')
lineWeights = weightout.readlines()
weightout.close()

nW=0
nHypo=1
for index,l in enumerate(lineWeights):
    if index==0 : continue
    if l[0]==lineWeights[index-1][0] : continue
    nHypo+=1
print "number of weights computed", len(lineWeights)/nHypo, "number of hypothesis tested :", nHypo

for h in range(0,nHypo):
    nev=0
    lhco = open('Events/DoubleDataA_537_mumu/input.lhco','r')
    for l in lhco:
        if l[0]!="0" : continue
        if nev < len(lineWeights) :
            l=l.strip()
            lineWeights[nW]=lineWeights[nW].strip()
            #print l, lineWeights[nev]
            info = l.split(" ",2)
            cut = lineWeights[nW].split("\t", 1)
            newline = str(h+1)+"."+info[2]+"."+info[1]+"\t"+cut[1]+"\n"
            out.write(newline)
            nW+=1
        nev+=1
    lhco.close()
out.close()

print "number of event in the lhco is :", nev
if nev==len(lineWeights) : print "all events computed"
else : "part of the events not used :", nev-len(lineWeights)

