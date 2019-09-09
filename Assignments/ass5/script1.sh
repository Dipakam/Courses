#!/bin/bash

# $1 is main.c file and $2 is input.txt file

#first we'll do the first job,line numbers and their frequency of execution
#creating the csv file  which will contain the outputs

echo Line,Frequency > linefreq.csv
echo >> linefreq.csv

gcc -fprofile-arcs -ftest-coverage -o a.out $1

#since gcov is cumulative, we can just run all the testcases first and collect the gcov files later
while IFS= read line
do
./a.out $line
done < "$2"

gcov $1

#now we have $1.gcov file which has all our required information, now to extract and print in linefreq

awk -v OFS="," -F ':' '{print $2, $1}' $1.gcov | tr -d " " >> linefreq.csv

gcov -b $1

grep -n "branch  0" sum.c.gcov >> textfile.txt

awk -v OFS="," -F[: ] '{print $1, $5}' $1.gcov | tr -d " " >> branchfreq.csv
