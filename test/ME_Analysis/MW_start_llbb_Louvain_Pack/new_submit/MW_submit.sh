#! /bin/sh

mkdir -p condor
rm -r submit.cmd tmp/ submit.cmd
./bin/madweight.py -12345
echo "MW run : directories ready"
bash new_submit/split.sh $1 $2 
bash new_submit/submit.sh 
echo "start submission jobs"
condor_submit submit.cmd 

