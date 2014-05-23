path=$1
num_events=$2

find $PWD/$path -type d -name event\* | sort -n > list
mkdir -p tmp
split -l $num_events list tmp/job
rm -f list
