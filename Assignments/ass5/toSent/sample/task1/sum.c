#include<stdio.h>
#include<stdlib.h>

int main(){

    int a=-5,i,sum=0,even=0;
    while (a < 5){
        a++;
        sum = even = 0;
        if (a < 0 ){
            printf("Should be a positive number\n");
            continue;
        }

        for(i = 1; i <= a; i++){
            sum += i;
            if (i % 4 == 0){
                even++;
            }
        }
        printf("sum = %d\n",sum);
    }
    return 0;
}
