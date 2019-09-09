#!/bin/bash
numlines=$(cat $1 |wc -l)
echo 'b add'>gdbscript.gdb
echo 'b sub'>>gdbscript.gdb
echo 'b mul'>>gdbscript.gdb
echo 'b divide'>>gdbscript.gdb
echo 'r'>>gdbscript.gdb
cur=1
while [ $cur -le $numlines ]
do
	((cur++))
	echo 'i r'>>gdbscript.gdb
	echo 'c'>>gdbscript.gdb
done
gdb -x gdbscript.gdb --args main $1
for i in $(cat gdbscript.gdb)
do
	$i
done
q


