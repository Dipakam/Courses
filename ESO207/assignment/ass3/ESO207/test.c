#include<stdio.h>
int main(){
  int Array[4];
  Array[0]=1;
  Array[1]=2;
  Array[2]=3;
  Array[3]=4;
  int size=4;
  int key=5;
  int arr[size+1][key+1];
  for(int i=0;i<size+1;i++){
    arr[i][0]=1;
  }
  for(int i=1;i<key+1;i++){
    arr[0][i]=0;
  }
  for(int i=1;i<size+1;i++){
    for(int j=1;j<key+1;j++){
      if(j<Array[i-1]){
        arr[i][j]=arr[i-1][j];
      }
      else{
        arr[i][j]=arr[i-1][j]+arr[i-1][j-Array[i-1]];
      }
    }
  }
  printf("%d\n",arr[size][key] );
}
