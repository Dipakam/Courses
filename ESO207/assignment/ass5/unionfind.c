#include<stdio.h>
#include<stdlib.h>
struct node {
  int element;
  int set;
  struct node * next;
};
typedef struct node node;
node * createnode(int keyi,int seti){
  node * Node = NULL;
  Node = (node *) malloc (1 * sizeof(node));
  Node -> element = keyi;
  Node -> set = seti;
  Node -> next = NULL;
  return Node;
}
int main(){
  int n,m;
  scanf("%d %d\n",&n,&m );
  node * Element[n];
  node * Set[n];
  int size[n];
  for(int i=0;i<n;i++){
    Element[i] = createnode(i,i);
    Set[i] = Element[i];
    size[i] = 1;
  }
  int a,b,c;
  for(int j = 0 ; j < m ;j++){
    scanf("%d",&a );
    if(a == 1){//union find
      scanf("%d %d\n",&b,&c );
      if(Element[b] -> set == Element[c] -> set){
        printf("0\n" );
      }
      else{
        int setb = Element[b] -> set;
        int setc = Element[c] -> set;
        if(size[setb] <= size[setc]){//b smaller
          node * curr = Set[setb];
          if(curr != NULL){
            while(curr -> next != NULL){
              curr -> set = setc;
              curr = curr -> next;
            }
            curr -> set = setc;
            curr -> next = Set[setc];
            Set[setc] = Set[setb];
            Set[setb] = NULL;
            size[setc] += size[setb];
            size[setb] = 0;
            printf("1\n");
          }
          else{//one of the sets is empty
            printf("1\n");
          }
        }
        else{//c is smaller

          node * curr = Set[setc];
          if(curr){
            while(curr -> next != NULL){
              curr -> set = setb;
              curr = curr -> next;
            }
            curr -> set = setb;
            curr -> next = Set[setb];
            Set[setb] = Set[setc];
            Set[setc] = NULL;
            size[setb] += size[setc];
            size[setc] = 0;
            printf("1\n");
          }
          else{//one of the sets is empty
            printf("1\n");
          }
        }
      }
    }
    else if(a == 2){//Find identity
      scanf("%d\n",&b );
      printf("%d\n",Element[b] -> set );
    }
    else if(a==3){
      scanf("%d %d\n",&b,&c );
      if(Element[b] -> set == Element[c] -> set){
        printf("1\n" );
      }
      else{
        printf("0\n" );
      }
    }
  }
return 0;

}
