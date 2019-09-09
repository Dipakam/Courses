gcc -pg -w -o "test" "tcas.c"
while read line; do
	./test $line > /dev/null
done < "testcase.txt"
gprof -bq "test" | tr -s " " > "temp.txt"
flag=0
function1name=""
function1time=0
echo "funtion1,timespent,function2,timespent" > "gprof.txt"
while read line;do
	Id="$(cut -d ' ' -f 1 <<< "$line")"
	if [[ $Id == "-----------------------------------------------" ]];
	then
		flag=0
	fi

	if [[ $flag == "1" ]];
	then
		function2name="$(cut -d ' ' -f 4 <<< "$line")"
		function2time="$(cut -d ' ' -f 1 <<< "$line")"
		if [[ $function1time =~ "[" ]];then
			continue
		else
			echo $function1name,$function1time,$function2name,$function2time >> "gprof.txt"
		fi
	fi
	if [[ $Id =~ "[" ]];
	then
		flag=1
		function1name="$(awk '{print $(NF-1)}' <<< "$line")"
		function1time="$(cut -d ' ' -f 3 <<< "$line")"
	fi 
done < temp.txt
cat gprof.txt