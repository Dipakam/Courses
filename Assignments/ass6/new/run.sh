#!/bin/bash

#for example, $1 is tcas.c
#and $2 is the file with test inputs, for example tcase.txt

inputfile="$1"
counter=0


while read line; do
	((counter++))
	gcc -fprofile-arcs -ftest-coverage -o "test" $inputfile	
        ./test $line         
	gcov -b $inputfile
	linenum=""
	linenum_buffer=""
	echo "line,freq" > "freq$counter.txt"
	echo "line,bias" > "bias$counter.txt"
	while read line; do
        	linenum="$(cut -d ":" -f 2 <<< $line)"
        	linefreq="$(cut -d ":" -f 1 <<< $line)"
        	if [[ $linefreq != $linenum ]];
        	then
			linenum_buffer=$linenum
                	if [[ $linefreq =~ "-" || $linefreq =~ "##" ]];
                	then
	                	continue
	                else
	                        echo $linenum,$linefreq >> "freq$counter.txt"
	                fi
	        fi
	        if [[ $line =~ "fallthrough" ]];
	        then
	                fin="$(cut -d " " -f 5 <<< $line)"
	                ffin="$(cut -d "%" -f 1 <<< $fin)"
	                echo $linenum_buffer,$ffin >> "bias$counter.txt"
	        fi
	done < $inputfile".gcov"				
done < "$2"
echo "" > bias.csv
tail -n +2 bias1.txt|awk -F"," '{print $1",1,"$2}' >>bias.csv
tail -n +2 bias2.txt|awk -F"," '{print $1",2,"$2}' >>bias.csv
tail -n +2 bias3.txt|awk -F"," '{print $1",3,"$2}' >>bias.csv
tail -n +2 bias4.txt|awk -F"," '{print $1",4,"$2}' >>bias.csv
tail -n +2 bias5.txt|awk -F"," '{print $1",5,"$2}' >>bias.csv

R -f facet.r
#R -r facet2.r
eog bias.jpg
