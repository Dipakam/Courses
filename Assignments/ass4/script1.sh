gcc -c add.c -o add.o
gcc -c sub.c -o sub.o
gcc -c -fPIC mpy.c -o mpy.o
gcc -c -fPIC divd.c -o divd.o
ar rcs ./libas.a ./add.o ./sub.o
gcc -shared ./mpy.o ./divd.o -o ./libmd.so
gcc -g -L$(pwd) -o main main.c libas.a -lmd
LD_LIBRARY_PATH=$(pwd)
export LD_LIBRARY_PATH=$(pwd):$LD_LIBRARY_PATH
./main $1
