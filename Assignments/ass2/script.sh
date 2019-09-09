#!/bin/bash

ps -eo cmd,pid,comm |grep "/bin/*\|/usr/bin/*" >proc
#lines = $(cat proc|wc -l)

while IFS= read -r line
do
    echo "$line" >Line
    #echo "new line"
    add= cut -d " " -f 1 Line
    echo "$add"
    comman= 'ls -l "$add"'
    #$comman
    echo "$comman"
  done<"proc"
