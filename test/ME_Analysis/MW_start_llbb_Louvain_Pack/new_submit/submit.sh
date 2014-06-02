
cp `dirname $0`/condor_head.cmd submit.cmd

for i in $PWD/tmp/job*
do 
    echo "arguments = $i" >> submit.cmd  
    echo "queue"          >> submit.cmd
    echo                  >> submit.cmd
done
