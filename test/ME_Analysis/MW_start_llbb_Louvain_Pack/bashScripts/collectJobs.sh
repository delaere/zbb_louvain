# script to collect jobs

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
    ./bin/madweight.py -8
    cd ..
  done
done
