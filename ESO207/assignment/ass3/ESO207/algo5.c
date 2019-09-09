#include<stdio.h>

int main(){
int T;
scanf("%d\n",&T );
for(int t=0;t<T;t++){
  int n;
  scanf("%d\n",&n );
  int N=2<<(n-1);
  int B[N];
  for(int i=0;i<N;i++){
    scanf("%d ",&B[i] );
  }
  int final[n];
  final[0]=B[1];
  if(n==1){
    printf("%d\n",B[1]);
    continue;
  }
  B[1]=0;
  int A[N];
  A[0]=B[0];
  A[1]=final[0];
  int countfinal=1;
  int countA=2;
  for(int i=2;i<N;i++){
    if(B[i]==0){
      continue;
    }
    else{
      final[countfinal]=B[i];
      countfinal++;
      int k=countA;
      for(int j=0;j<countA;j++){
        A[k]=A[j]+B[i];
        k++;
      }
      int del=countA;
      countA=k;
      for(k=del;k<countA;k++){
        for(int l=0;l<N;l++){
          if(B[l]==A[k]){
            B[l]=0;
            //k++;
            break;
          }
        }
      }
    }
  }
  for(int i=0;i<n-1;i++){
    printf("%d ", final[i]);
  }
  printf("%d\n",final[n-1] );

}
  return 0;
}
