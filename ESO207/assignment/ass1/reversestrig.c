#include<stdio.h>
#include<string.h>
int main(){
  char s[100],r[100];
  fgets(s,100,stdin);
  //printf("%s\n",strrev(s) );

  int count = 0,begin,end=0;
  while (s[count] != '\0')
      count++;

   end = count - 1;

   for (begin = 0; begin < count; begin++) {
      r[begin] = s[end];
      end--;
   }

   r[begin] = '\0';

   printf("%s\n",r );
  return 0;
}
