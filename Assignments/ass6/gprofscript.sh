#!/bin/bash
gcc -pg $1
./a.out
gprof -bq a.out gmon.out >callgraph.txt
echo "function,time" >gprof.csv
cat callgraph.txt | head -n -5|tail -n +7|grep -G "^\["|tr -s " "|awk '{print $(NF-1)","$3}' >>gprof.csv
R -f column.r
eog gprof.jpg
