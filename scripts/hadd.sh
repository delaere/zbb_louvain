#! /bin/sh

n=30
list=$1

i=1
first=1
lines=`wc -l $list | awk '{ print $1 }'`

while [ $first -lt $lines ]
do
   last=`expr $first + $n`
   selection=`sed "$first,$last!d" $list`
   hadd result_temp_$i.root $selection
   first=`expr $first + $n + 1`
   i=`expr $i + 1`
done

hadd result_final.root result_temp_*.root

