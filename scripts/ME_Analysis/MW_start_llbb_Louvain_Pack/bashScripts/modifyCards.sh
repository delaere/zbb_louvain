#script to modify cards for general parameters

channels=(mumu ee)

for c in ${channels[*]}
do
  cd ggZbb_${c}
  cp ../replace.py .
  python replace.py Cards/run_card.dat 7000 4000
  python replace.py Cards/MadWeight_card.dat madgraph==True CMSFARM==True
  python replace.py Cards/MadWeight_card.dat "cluster              0" "cluster              1"
  python replace.py Cards/MadWeight_card.dat "13       180" "13       172.5"
  python replace.py Cards/MadWeight_card.dat "13       190" "#13       190"
  python replace.py Cards/param_card.dat 1.730000e+02 1.725000e+02
  python replace.py Cards/param_card.dat 1.200000e+02 1.250000e+02
  rm replace.py
  cd ../qqZbb_${c}
  cp ../replace.py .
  python replace.py Cards/run_card.dat 7000 4000
  python replace.py Cards/MadWeight_card.dat madgraph==True CMSFARM==True
  python replace.py Cards/MadWeight_card.dat "cluster              0" "cluster              1"
  python replace.py Cards/MadWeight_card.dat "13       180" "13       172.5"
  python replace.py Cards/MadWeight_card.dat "13       190" "#13       190"
  python replace.py Cards/param_card.dat 1.730000e+02 1.725000e+02
  python replace.py Cards/param_card.dat 1.200000e+02 1.250000e+02
  rm replace.py
  cd ../ttbar_${c}
  cp ../replace.py .
  python replace.py Cards/run_card.dat 7000 4000
  python replace.py Cards/MadWeight_card.dat madgraph==True CMSFARM==True
  python replace.py Cards/MadWeight_card.dat "cluster              0" "cluster              1"
  python replace.py Cards/MadWeight_card.dat "isr                  0" "isr                  2"
  python replace.py Cards/MadWeight_card.dat "13       180" "13       172.5"
  python replace.py Cards/MadWeight_card.dat "13       190" "#13       190"
  python replace.py Cards/param_card.dat 1.730000e+02 1.725000e+02
  python replace.py Cards/param_card.dat 1.200000e+02 1.250000e+02
  rm replace.py
  cd ../ZZ_C0_${c}
  cp ../replace.py .
  python replace.py Cards/run_card.dat 7000 4000
  python replace.py Cards/MadWeight_card.dat madgraph==True CMSFARM==True
  python replace.py Cards/MadWeight_card.dat "cluster              0" "cluster              1"
  python replace.py Cards/MadWeight_card.dat "13       180" "13       172.5"
  python replace.py Cards/MadWeight_card.dat "13       190" "#13       190"
  python replace.py Cards/param_card.dat 1.730000e+02 1.725000e+02
  python replace.py Cards/param_card.dat 1.200000e+02 1.250000e+02
  rm replace.py
  cd ../ZZ_C3_${c}
  cp ../replace.py .
  python replace.py Cards/run_card.dat 7000 4000
  python replace.py Cards/MadWeight_card.dat madgraph==True CMSFARM==True
  python replace.py Cards/MadWeight_card.dat "cluster              0" "cluster              1"
  python replace.py Cards/MadWeight_card.dat "isr                  0" "isr                  3"
  python replace.py Cards/MadWeight_card.dat "13       180" "13       172.5"
  python replace.py Cards/MadWeight_card.dat "13       190" "#13       190"
  python replace.py Cards/param_card.dat 1.730000e+02 1.725000e+02
  python replace.py Cards/param_card.dat 1.200000e+02 1.250000e+02
  rm replace.py
  higgsHypo=(123 456 789)
  for h in ${higgsHypo[*]}
    do
    cd ../ZH_C0_${h}_${c}
    cp ../replace.py .
    python replace.py Cards/run_card.dat 7000 4000
    python replace.py Cards/MadWeight_card.dat madgraph==True CMSFARM==True
    python replace.py Cards/MadWeight_card.dat "cluster              0" "cluster              1"
    python replace.py Cards/MadWeight_card.dat "12       6" "12       25"
    python replace.py Cards/MadWeight_card.dat "13       180" "13       125"
    python replace.py Cards/MadWeight_card.dat "13       190" "#13       190"
    python replace.py Cards/param_card.dat 1.730000e+02 1.725000e+02
    python replace.py Cards/param_card.dat 1.200000e+02 1.250000e+02
    python replace.py Cards/param_card.dat 5.753088e-03 2.500000e+00 
    rm replace.py
    cd ../ZH_C3_${h}_${c}
    cp ../replace.py .
    python replace.py Cards/run_card.dat 7000 4000
    python replace.py Cards/MadWeight_card.dat madgraph==True CMSFARM==True
    python replace.py Cards/MadWeight_card.dat "cluster              0" "cluster              1"
    python replace.py Cards/MadWeight_card.dat "isr                  0" "isr                  3"
    python replace.py Cards/MadWeight_card.dat "12       6" "12       25"
    python replace.py Cards/MadWeight_card.dat "13       180" "13       125"
    python replace.py Cards/MadWeight_card.dat "13       190" "#13       190"
    python replace.py Cards/param_card.dat 1.730000e+02 1.725000e+02
    python replace.py Cards/param_card.dat 1.200000e+02 1.250000e+02
    python replace.py Cards/param_card.dat 5.753088e-03 0.160000e+00 
    rm replace.py
  done
done

cd ..