#Check for correct number of arguments
if [ $# -lt 2 ]
then
    echo "Script needs 2 arguments : one for the name, one for the number of events/jobs"
    exit
fi

# 2 args, one for the name, one for the number of events/jobs
proc=$1
nWs=$2

processes=(ggZbb qqZbb ttbar ZZ_C0 ZZ_C3 ZH_C0_123 ZH_C3_123 ZH_C0_456 ZH_C3_456 ZH_C0_789 ZH_C3_789)
#processes=(ZH_C0_123 ZH_C3_123 ZH_C0_456 ZH_C3_456 ZH_C0_789 ZH_C3_789)
#processes=(ZH_C3_456 ZH_C3_789)
channels=(mumu ee)
#channels=(ee)

for p in ${processes[*]}
do
  name=$p
  for c in ${channels[*]}
  do
    name_=${name}_$c
    echo ${name_}
    cd ${name_}
    #./bin/madweight.py -12345
    ./new_submit/MW_submit.sh SubProcesses/P0_*/${proc}_$c/ $nWs
    cd ..

  done
done
