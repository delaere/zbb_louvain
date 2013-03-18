#script to copy the TFs from MW_start_llbb_Louvain_Pack and to copy new_submit directory
#copy MadWeight_card.dat to falcilitate replacing of the card

processes=(ggZbb qqZbb ttbar ZZ_C0 ZZ_C3 ZH_C0_123 ZH_C3_123 ZH_C0_456 ZH_C3_456 ZH_C0_789 ZH_C3_789)
#processes=(ZH_C0_123 ZH_C3_123 ZH_C0_456 ZH_C3_456 ZH_C0_789 ZH_C3_789)
channels=(mumu ee)

for p in ${processes[*]}
do
  name=$p
  for c in ${channels[*]}
  do
    name_=${name}_$c
    echo ${name_}
    cp MW_start_llbb_Louvain_Pack/Transfer_function_pack/* ${name_}/Source/MadWeight/transfer_function/data/.
    cp -r MW_start_llbb_Louvain_Pack/new_submit/ ${name_}/.
    cp ${name_}/Cards/MadWeight_card.dat ${name_}/copyOfMWcard.txt
  done
done
