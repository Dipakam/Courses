#include<stdio.h>
#include<stdlib.h>
#include "add.h"
#include "sub.h"
#include "mpy.h"
#include "divide.h"

int main(int argc, char *argv[]){
	if(argc==0){
		printf("please specify the file name");
		return 0;
	}
	if(argc>2){
		printf("%d %s", argc , argv[1]);
		printf("too many arguments");
		return 0;
	}
	

	double a;
	double b;
	FILE * fo =fopen(argv[1],"r");
	char astring[20];
	char op;
	char bstring[20];
	while(fscanf(fo,"%s",astring)!=EOF){
		fscanf(fo," %c ",&op);
		fscanf(fo,"%s\n",bstring);
		a=atof(astring);
		b=atof(bstring);
		if(op=='+'){
			printf("%lf\n",add(a,b));
		}
		else if(op=='-'){
			printf("%lf\n",sub(a,b));
		}
		else if(op=='*'){
			printf("%lf\n",mul(a,b));
		}
		else if(op=='/'){
			printf("%lf\n",divide(a,b));
		}
		//printf("%lf \n %c \n %lf \n",a,op,b);
	}
	return 0;
}
