inputfile="tcas.c"

gcc -fprofile-arcs -ftest-coverage -o "test" $inputfile
while read line; do
        ./test $line
done < "testcase.txt"
gcov -b $inputfile
linenum=""
linenum_buffer=""
echo "line,freq" > "freq.txt"
echo "line,bias" > "bias.txt"
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
                        echo $linenum,$linefreq >> "freq.txt"
                fi
        fi
        if [[ $line =~ "fallthrough" ]];
        then
                fin="$(cut -d " " -f 5 <<< $line)"
                ffin="$(cut -d "%" -f 1 <<< $fin)"
                echo $linenum_buffer,$ffin >> "bias.txt"
        fi
done < $inputfile".gcov"
