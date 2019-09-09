#include<stdio.h>
#include<stdlib.h>
void PrintArray(int ** array,int size) {
  for(int i=0;i<size;i++){
    printf("%d %d\n",array[i][0],array[i][1] );
  }
  return;
}
void PrintArrayCopy(int array[][2],int size) {
  for(int i=0;i<size;i++){
    printf("%d %d\n",array[i][0],array[i][1] );
  }
  return;
}
void Merge(int arr1[][2],int arr2[][2],int size1,int size2,int ** final){
  int cur1=0,cur2=0,cur=0;
  int size = size1+size2;
  /*printf("Stsrt\n" );
  PrintArrayCopy(arr1,size1);
  PrintArrayCopy(arr2,size2);*/
  for(int i=0;i<size;i++){
    if(cur1==size1){
      for(int j=cur2;j<size2;j++){
        final[cur][0]=arr2[j][0];
        final[cur][1]=arr2[j][1];
        cur++;
      }
      break;
    }
    else if(cur2==size2){
      for(int j=cur1;j<size1;j++){
        final[cur][0]=arr1[j][0];
        final[cur][1]=arr1[j][1];
        cur++;
      }
      break;
    }
    else{
      if(arr1[cur1][0]>=arr2[cur2][0]){
        if (arr1[cur1][0]==arr2[cur2][0]) {
          if(arr1[cur1][1]>=arr2[cur2][1]){
            final[cur][0]=arr2[cur2][0];
            final[cur][1]=arr2[cur2][1];
            cur2++;
            cur++;
            continue;
          }
          else{
            final[cur][0]=arr1[cur1][0];
            final[cur][1]=arr1[cur1][1];
            cur1++;
            cur++;
            continue;
          }
        }
        final[cur][0]=arr2[cur2][0];
        final[cur][1]=arr2[cur2][1];
        cur2++;
        cur++;
      }
      else{
        final[cur][0]=arr1[cur1][0];
        final[cur][1]=arr1[cur1][1];
        cur1++;
        cur++;
      }
    }
  }
  /*printf("OP from function\n");
  PrintArray(final,size);*/
}
void Sort(int array[][2],int start,int end,int ** final){
  int size = end-start+1;
  if(end==start){
    return;
  }
  Sort(array,start,(start+end)/2,final);
  Sort(array,(start+end)/2+1,end,final);
  //printf("First half\n");
  //PrintArrayCopy(array+start,1+(end-start)/2);
  //printf("Second Half\n");
  //PrintArrayCopy(array+(start+end)/2+1,size-1-(end-start)/2);*/
  for(int i=start;i<=end;i++){
    array[i][0]=final[i][0];
    array[i][1]=final[i][1];
  }
  /*printf("Copying the elements\n");
  PrintArrayCopy(array+start,size);*/
  Merge(array+start,array+(start+end)/2+1,1+(end-start)/2,size-1-(end-start)/2,final+start);
  /*printf("Full array\n");

  PrintArray(final+start,size);*/
  return;
}
int IsDom(int x1,int y1,int x2,int y2){
  if(x1==x2&&y1==y2){
    return 0;
  }
  else if(x1>=x2&&y1>=y2){
    return 1;
  }
  else if(x1<=x2&y1<=y2){
    return 2;
  }
  else{
    return 3;
  }
}
int MergeDom(int **A,int **B,int sizeA,int sizeB,int ** final){
  int cur=0;
  int indB=0;
  int ind=0;
  int excluded_ind[sizeB];
  /*printf("Array B\n" );
  PrintArray(B,sizeB);*/
  for(int i=0;i<sizeA;i++){
    if(IsDom(A[i][0],A[i][1],B[indB][0],B[indB][1])==2){
      break;
    }
    else if(IsDom(A[i][0],A[i][1],B[indB][0],B[indB][1])==3){
      final[cur][0]=A[i][0];
      final[cur][1]=A[i][1];
      //printf("3 :cur =%d\n",cur );
      cur++;
    }
    else if(IsDom(A[i][0],A[i][1],B[indB][0],B[indB][1])==1){
      final[cur][0]=A[i][0];
      final[cur][1]=A[i][1];
      cur++;
      excluded_ind[ind]=indB;
      ind++;
      indB++;
      //printf("1: cur=%d",cur);
      if(indB==sizeB){
        break;
      }
    }
    else if(IsDom(A[i][0],A[i][1],B[indB][0],B[indB][1])==0){
      excluded_ind[ind]=indB;
      indB++;
      ind++;
    }

  }
  /*printf("These were excluded \n %d",ind );
  for(int i=0;i<ind;i++){
    printf("%d %d\n",B[excluded_ind[i]][0],B[excluded_ind[i]][1] );
  }*/
  //printf("Cur=%d ,Array B \n",cur );
  //PrintArray(B,sizeB);
  int alt_ind=0;
  for(int j=0;j<sizeB;j++){
    if(ind>0&&j==excluded_ind[alt_ind]){
      alt_ind++;
      continue;
    }
    final[cur][0]=B[j][0];
    final[cur][1]=B[j][1];
    cur++;
  }
  return cur;
}
int Dom(int ** A,int size,int **B){
  if(size==1){
    B[0][0]=A[0][0];
    B[0][1]=A[0][1];
    //PrintArray(A,1);
    //printf("1 on call\n" );
    return size;
  }
  else{
    int size1 = size/2;
    int size2 = size - size1;
    int ** A1;
    int ** A2;
    A1=(int **)malloc(size1*sizeof(int *));
    for(int i=0;i<size1;i++){
      A1[i]=(int *)malloc(2*sizeof(int));
    }
    A2=(int **)malloc(size2*sizeof(int *));
    for(int i=0;i<size2;i++){
      A2[i]=(int *)malloc(2*sizeof(int));
    }

    int size1a = Dom(A,size1,A1);
    int size2a = Dom(A+size1,size2,A2);
    size = MergeDom(A1,A2,size1a,size2a,B);
    /*printf("First Part\n");
    PrintArray(A1,size1a);
    printf("Second Part\n");
    PrintArray(A2,size2a);
    printf("merged part\n");
    PrintArray(B,size);*/
    for(int i=0;i<size1;i++){
      free(A1[i]);
    }
    for(int j=0;j<size2;j++){
      free(A2[j]);
    }
    free(A1);
    free(A2);
    //printf("%d on the call\n",size );
    return size;

  }
}
int main(){
  int N;
  scanf("%d",&N );
  int A[N][2];
  for(int i=0;i<N;i++){
    scanf("%d",&A[i][0]);
    scanf("%d",&A[i][1]);
  }
  //PrintArray(A,N);
  int ** final,** finalc;
  final = (int **)malloc(N*sizeof(int *));
  finalc = (int **)malloc(N*sizeof(int *));
  for(int i=0;i<N;i++){
    final[i] = (int *)malloc(2*sizeof(int));
    finalc[i] = (int *)malloc(2*sizeof(int));
  }
  for(int i=0;i<N;i++){
    final[i][0]=A[i][0];
    final[i][1]=A[i][1];
  }
  Sort(A,0,N-1,final);
  int size = Dom(final,N,finalc);
  //printf("%d :size \n",size );
  //printf("finalc\n" );
  PrintArray(finalc,size);
  /*printf("Initial\n");
  PrintArray(final,N);*/
  for(int i=0;i<N;i++){
    free(*(final+i));
    free(*(finalc+i));
  }
  free(final);
  free(finalc);
  return 0;
}
