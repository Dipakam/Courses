#!/bin/bash

while IFS= read -r line do
	gcc -fprofile-arcs -ftest-coverage $1
	./a.out $line
	gcov -b $1.gcov
	cat tcas.c.gcov | grep -n "fallthrough" >>fallthrough.txt
	echo "line bias">bias.csv
	for i in $(cat fallthrough.txt|cut -d ":" -f1) do
		j=$((i-1))
		linenum=$(sed -n "$j"p $1.gcov|cut -d ":" -f2|tr -s " ")
		linebias=$(sed -n "$i"p $1.gcov|tr -s " "|cut -d " " -f4)
		echo $linenum," ",$linebias >> bias.csv
	done
	join final.csv bias.csv > final.csv

done <$2
cut -d " " -f1,2,3,4,5,6 --output-delimiter="," final.csv 
