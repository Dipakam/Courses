#include<stdio.h>

int main(){
  int T;
  scanf("%d\n",&T );
  for (int i=0;i<T;i++){
    int n;
    scanf("%d\n",&n );
    int N=2<<(n-1);
    int B[N][2];
    for(int j=0;j<N;j++){
      scanf("%d",&B[j][0] );
      B[j][1]=1;
    }
    int l=1;
    B[0][1]=0;
    int C[N];

    int countC=2;
    C[0]=0;
    C[1]=1;

    int final[n];
    final[0]=B[1][0];
    int count=1;
    for(l=2;l<N;l++){
      if(B[l][1]==0){
        continue;
      }
      else{

        int x=B[l][0];
        int temp[countC];

        int countTemp=0;
        for(int m=0;m<countC;m++){

          int man=C[m];
          temp[countTemp]=B[man][0]+x;
          printf("%d %d %d %d\n",C[m],B[man][0],x,countTemp );
          countTemp++;
        }
        printf("%d\n",temp[countTemp-1] );
        /*for(int index=0;index<countC;index++){
          printf("%d\n",temp[index]);
          //printf("%d %d\n",B[index][0],B[index][1]);
        }*/
        //countC=countC+countTemp;
        int Temp=0;
        for(int d=i;d<N;d++){
          if(B[d][1]==1){
            int flag=0;
            for(int ind=0;ind<countTemp;ind++){
              if(B[d][0]==temp[ind]){
                flag=1;
                break;
              }
            }
            if(flag==1){
              B[d][1]=0;
              final[count]=B[d][0];
              count++;
              C[countC]=d;
              countC++;
            }

          }
        }
      }
    }
    for(int i=0;i<n-1;i++){
      printf("%d ",final[i]);
    }
    printf("%d\n",final[n-1] );

  }
}
