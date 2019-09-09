#include<stdio.h>
#include<stdlib.h>
/*int BinarySearch(int B[][2],int key,int N,int start,int end){
  int mid=(start+end)/2;
  for(int i=start;i<=end;i++){
    printf("%d\n",B[i][0] );
  }
  int index=0;
  if(start==end){
    if(B[start][0]==key ){
      if(B[start][1]==1){
        B[start][1]==0;
        return start;
      }
      else{
        for(int i=start;i<N-1;i++){
          if(B[i][0]==key ){
            if(B[i][1]==1){
              B[i][1]=0;
              return i;
            }
          }
          else{
            return 0;
            break;
          }
        }
      }
    }
    else{
      return 0;
    }
  }
  if(B[mid][0]>key || (B[mid][0]==key && B[mid][1]==0)){
    return BinarySearch(B,key,N/2,start,mid);
  }
  else if(B[mid][0]<key){
    return BinarySearch(B,key,N/2,mid+1,end);
  }
  else{
    index=mid;
    for(int i=mid;i>start;i--){
      if(B[i-1][0]==key && B[i-1][1]==1){
        if(B[i][1]==1){
          index=i-1;

        }
      }
    }
    B[index][1]=0;
    return index;
  }
}*/
void printArray(int A[],int size){
  for(int i=0;i<size;i++){
    printf("%d ",A[i] );
  }
  printf("\n");
  return ;
}
int Search(int B[][2],int key,int size){
  for(int i=0;i<size;i++){
    if(B[i][0]==key && B[i][1]==1){
      B[i][1]=0;
      return i;
    }
  }
}
int main(){
  int T;
  scanf("%d\n",&T );
  for(int t=0;t<T;t++){
    int n;
    scanf("%d",&n );
    int A[n];
    int N=2<<(n-1);
    //printf("%d\n",N );
    int B[N][2];
    /*int **B;
    B=(int **)malloc(N*sizeof(int *));
    for(int z=0;z<N;z++){
      B[z]=(int *)malloc(2*sizeof(int));
    }*/
    for(int j=0;j<N;j++){
      scanf("%d",&B[j][0] );
      B[j][1]=1;
    }
    A[0]=B[1][0];
    B[0][1]=0;
    B[1][1]=0;
    int countA=1;
    int C[N];
    C[0]=0;
    C[1]=1;
    int countC=2;
    for(int j=2;j<N;j++){
      if(B[j][1]==0){
        continue;
      }
      else{
        int x=B[j][0];
        A[countA]=x;
        countA++;
        if(countA==n){
          break;
        }
        B[j][1]=0;
        int Temp[countC-1];
        int flag=0;
        for(int h=0;h<countC;h++){
          if(C[h]==j){
            flag=1;
            break;
          }
        }
        if(flag==0){
          C[countC]=j;
          countC++;
        }

        int countTemp=0;
        for(int i=1;i<countC-1;i++){
          int index=C[i];
          Temp[countTemp]=x+B[index][0];
          countTemp++;
        }
        for(int i=0;i<countTemp;i++){
          int ind=Search(B,Temp[i],N);
          //printf("%d %d\n",Temp[i],ind );
          int flag=0;
          for(int h=0;h<countC;h++){
            if(C[h]==j){
              flag=1;
              break;
            }
          }
          if(flag==0){
            C[countC]=ind;
            countC++;
          }
        }
        //printArray(C,countC);
        //printArray(A,countA);
        //printArray(Temp,countTemp);
      }
    }
    printArray(A,n);
  }
  return 0;
}
