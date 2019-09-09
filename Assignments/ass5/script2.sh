#!/bin/bash
gcc -pg $1 -o run 1 > /dev/null
while IFS= read line
do
	./run $line 2 > /dev/null
	gprof -q -b run gmon.out > callgraph.txt
	echo 'Test Case : ' >> output
	echo $line >> output
	python3 reshape.py >> output
done <$2
