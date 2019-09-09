#include<stdio.h>
int SumGeneratable(long Array[],int size,long key){
  int arr[size+1][key+1];
  for(int i=0;i<size+1;i++){
    arr[i][0]=1;
  }
  for(long i=1;i<key+1;i++){
    arr[0][i]=0;
  }
  for(int i=1;i<size+1;i++){
    for(long j=1;j<key+1;j++){
      if(j<Array[i-1]){
        arr[i][j]=arr[i-1][j];
      }
      else{
        arr[i][j]=arr[i-1][j]+arr[i-1][j-Array[i-1]];
      }
    }
  }
  return arr[size][key];
}
int main(){
  int T;
  scanf("%d\n",&T );
  for (int t=0;t<T;t++){
    int n;
    scanf("%d\n",&n );
    int N=2<<(n-1);
    long B[N];
    for(int j=0;j<N;j++){
      scanf("%ld",&B[j] );
    }
    long A[n];
    A[0]=B[1];
    int count =1;
    int x;
    for(int i=2;i<N;i++){
      if(B[i]!=B[i-1]){
        x=SumGeneratable(A,count,B[i]);
        if(x>0){
          x=x-1;
          continue;
        }
        else{
          A[count]=B[i];
          count++;
          if(count==n){
            break;
          }
        }
      }
      else{
        x=x-1;
        if(x>0){
          x=x-1;
          continue;
        }
        else{
          A[count]=B[i];
          count++;
          if(count==n){
            break;
          }
        }
      }
    }
    for(int k=0;k<count-1;k++){
      printf("%ld ",A[k] );
    }
    printf("%ld\n",A[count-1] );
  
  }
  return 0;
}

