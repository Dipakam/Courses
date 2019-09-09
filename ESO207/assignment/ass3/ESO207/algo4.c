#include<stdio.h>
#include<stdlib.h>
void printArray(int A[],int size){
  for(int i=0;i<size;i++){
    printf("%d ",A[i] );
  }
  printf("\n");
  return ;
}
int Search(int A[],int key,int n,int times){

  int N=2<<(n-2);
  int C[N];
  C[0]=0;
  C[1]=A[0];
  for(int i=2;i<n+1;i++){
    int k=2<<(i-2);
    int z=k;
    for(int j=0;j<k;j++){
      C[z]=C[j]+A[i-1];
      z++;
    }
  }
  for(int i=0;i<n;i++){
    if(C[i]==key){
      times--;
    }
  }
  return times;
}
int main(){
  int T;
  scanf("%d\n",&T );
  for(int t=0;t<T;t++){
    int n;
    scanf("%d",&n );
    int A[n];
    int N=2<<(n-1);
    int B[N];
    for(int j=0;j<N;j++){
      scanf("%d",&B[j] );
    }
    A[0]=B[1];
    int countA=1;
    for(int i=2;i<N;i++){
      int times=0;
      int j=i;
      for(j=i;j<N;j++){
        if(B[j]==B[i]){
          times++;
        }
        else{
          break;
        }

      }
      int x=Search(A,B[i],countA,times);
      if(x==1){
        A[countA]=B[i];
        countA++;
        if(countA==n){
          break;
        }
      }
      i=j-1;
    }
    printArray(A,n);
  }
  return 0;
}
