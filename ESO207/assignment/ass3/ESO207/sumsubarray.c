#include<stdio.h>
void printArray(int A[],int size){
  for(int i=0;i<size;i++){
    printf("%d ",A[i] );
  }
  printf("\n");
  return ;
}

int main(){
  int n;
  scanf("%d",&n );
  int A[n];
  int N=2<<(n-1);
  int B[N];
  for(int i=0;i<n;i++){
    scanf("%d",&A[i] );
  }
  B[0]=0;
  B[1]=A[0];
  for(int i=2;i<n+1;i++){
    int k=2<<(i-2);
    int z=k;
    for(int j=0;j<k;j++){
      B[z]=B[j]+A[i-1];
      z++;
    }
  }
  printArray(B,N);
}
