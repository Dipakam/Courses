#include<stdio.h>
int BinarySearch(int B[],int key,int N,int start,int end){
  int mid=(start+end)/2-1;
  int index=0;
  if(start==end){
    if(B[0]==key && B[0][1]==1){
      return start;
    }
    else{
      return 0;
    }
  }
  if(B[mid][0]>key || (B[mid][0]==key && B[mid][1]==0)){
    return BinarySearch(B,key,N/2,mid+1,end);
  }
  else if(B[mid][0]<key){
    return BinarySearch(B,key,N/2,start,mid);
  }
  else{
    for(int i=mid;i>0;i--){
      if(B[i-1][0]==key && B[i-1][1]==1){
        if(B[i][1]==1){
          index=i;

        }
      }
    }
    B[index][1]=0;
    return index;
  }
}
int main(){
  int T=1;
  //scanf("%d\n",&T );
  for(int t=0;t<T;t++){
    int n;
    scanf("%d",&n );
    int A[n];
    int N=2<<(n-1);
    //printf("%d\n",N );
    int B[N];
    for(int j=0;j<N;j++){
      scanf("%d",&B[j] );
      //B[j]=1;
    }
    printf("%d\n",BinarySearch(B,) );
  }
  return 0;
}
