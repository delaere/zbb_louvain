#script to change the follwing parmeters : name of the run, number of events to process, number of integration points

#source new_changeProcess.sh ttbar_V3 2984 2984 100000 TT_Mu_MC TT_El_MC
#source new_changeProcess.sh ZZ_V2 17792 11505 100000 ZZ_Mu_MC ZZ_El_MC
#source new_changeProcess.sh ZH125_V2 10000 10000 100000 ZH125_Mu_MC ZH125_El_MC
#source new_changeProcess.sh Data2012A_V2 1032 867 100000 MuA_DATA ElA_DATA
#source new_changeProcess.sh Data2012B_V2 5191 5002 100000 MuB_DATA ElB_DATA

#source new_changeProcess.sh DY_537 11876 8205 100000 DY_Mu_MC DY_El_MC
#source new_changeProcess.sh DoubleDataA_537 1145 923 100000 DoubleMu_DataA DoubleEle_DataA
#source new_changeProcess.sh DoubleDataA06aug_537 130 100 100000 DoubleMu_DataA06aug DoubleEle_DataA06aug
#source new_changeProcess.sh DoubleDataB_537 7441 5199 100000 DoubleMu_DataB DoubleEle_DataB
#source new_changeProcess.sh DoubleDataC-v2_537 10905 7751 100000 DoubleMu_DataC-v2 DoubleEle_DataC-v2
#source new_changeProcess.sh DoubleDataD_537 13736 9722 100000 DoubleMu_DataD DoubleEle_DataD

#Check for correct number of arguments
if [ $# -lt 6 ]
then
    echo "Script needs 8 arguments for comparison : source new_changeProcess.sh new_proc old_proc new_evts_mumu old_evts_mumu new_evts_ee old_evts_ee new_points old_points"
    exit
fi

# 8 args : name of the new/old process, new/old number of events to process, new/old number of integration points

new_proc=$1
new_evts_mumu=$2
new_evts_ee=$3
new_points=$4
mu=$5
el=$6

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
    cp ../replace.py .
    if [ $c == "mumu" ]
    then
	old_evts=5191
	new_evts=${new_evts_mumu}
	cp /nfs/user/acaudron/LHCO537/outCMStoLHCO${mu}V2_0.lhco Events/input.lhco
   else
	old_evts=5002
        new_evts=${new_evts_ee}
	cp /nfs/user/acaudron/LHCO537/outCMStoLHCO${el}V2_0.lhco Events/input.lhco
    fi
    cp copyOfMWcard.txt Cards/MadWeight_card.dat
    python replace.py Cards/MadWeight_card.dat "name                Data2012B"_$c "name                "${new_proc}_$c
    python replace.py Cards/MadWeight_card.dat "nb_exp_events        "${old_evts} "nb_exp_events        "${new_evts}
    python replace.py Cards/MadWeight_card.dat "MW_int_points        100000" "MW_int_points        "${new_points}
    rm replace.py
    cd ..

  done
done
