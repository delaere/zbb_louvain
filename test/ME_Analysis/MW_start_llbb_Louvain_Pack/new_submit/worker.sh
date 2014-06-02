#! /bin/sh

for dir in `cat $1`
do
  cd $dir
  ../../../comp_madweight
done

