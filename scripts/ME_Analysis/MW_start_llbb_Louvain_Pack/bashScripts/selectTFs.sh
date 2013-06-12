#script to select TFs

processes=(ggZbb qqZbb ttbar ZZ_C0 ZZ_C3 ZH_C0_123 ZH_C3_123 ZH_C0_456 ZH_C3_456 ZH_C0_789 ZH_C3_789)
#processes=(ZH_C0_123 ZH_C3_123 ZH_C0_456 ZH_C3_456 ZH_C0_789 ZH_C3_789)
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
    if [ $c == "mumu" ]
	then
	./bin/change_tf.py <<+EOF
arnaud_muon1pt
+EOF
    else
	./bin/change_tf.py << +EOF
arnaud
+EOF
    fi
    cd ..
    
  done
done
