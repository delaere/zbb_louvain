#! /bin/sh

mkdir -p condor
rm submit.cmd tmp/
bash new_submit/split.sh $1 $2 
bash new_submit/submit.sh 
condor_submit submit.cmd 

