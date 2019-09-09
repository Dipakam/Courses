#!/bin/bash
totallines=cat $1 |wc -l
gcc -fprofile-arcs -ftest-coverage $1
for i in $(cat $2)
do
	#./a.out $i 2>/dev/null
	#gcov -a $1
	echo $i
	#echo $totallines

	#tail -n $totallines "$1.gcov"
done	
