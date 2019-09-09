gcc -pg $1
./a.out
gprof -bq a.out gmon.out > output.txt
