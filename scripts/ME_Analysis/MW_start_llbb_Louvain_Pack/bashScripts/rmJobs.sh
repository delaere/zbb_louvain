#script to remove a run

#Check for correct number of arguments
if [ $# -lt 1 ]
then
    echo "Script needs 1 arguments : name of the run, example if run = ttbar_ee, argument should be ttbar"
    exit
fi

proc=$1

processes=(ggZbb qqZbb ttbar ZZ_C0 ZZ_C3 ZH_C0 ZH_C3)
channels=(mumu ee)

for p in ${processes[*]}
do
  name=$p
  for c in ${channels[*]}
  do
    name_=${name}_$c
    echo ${name_}
    cd ${name_}
    rm -rf SubProcesses/P0_*/${proc}_$c/
    cd ..
  done
done
