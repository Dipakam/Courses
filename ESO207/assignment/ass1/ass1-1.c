#include<stdio.h>
#include<stdlib.h>
struct numop{
  char type;
  char op;
  double num;
};

typedef struct numop numop;
struct node{
  numop * item;
  struct node * next;
};
typedef struct node node;
node * head=NULL;
int isEmpty(node * stack){
  if(stack==NULL){
    return 1;
  }
  else return 0;
}
void push(node * key){
  key->next = head;
  head = key;
  return;
}
numop * Top(){
  return head->item;
}
void deleteNode(node * key){
  free(key->item);
  free(key);
  return;
}
void Pop(){
  node * clear=head;
  head = clear->next;
  deleteNode (clear);
  return;
}

numop * CreateStack(){
  numop * pointer=NULL;
  return pointer;
}
node * CreateNode(numop * key){
  node * Node = NULL;
  Node = (node *)malloc(sizeof(node));
  Node->item = key;
  Node->next = NULL;
  return Node;
}
void PrintTop(){
  char ty = (Top())->type;
  if(ty=='c'){
    printf("%c\n",Top()->op);
  }
  else{
    printf("%lf\n",Top()->num);
  }
  return;
}
void InsertNum(int no){
  numop * input=CreateStack();
  input = (numop *)malloc(sizeof(numop));
  input->type = 'n';
  input->num = no;
  node * Node = CreateNode(input);
  push(Node);
  printf("$\n");
}
void InsertSymb(char sym){
  numop * input = CreateStack();
  input = (numop *)malloc(sizeof(numop));
  input->type = 'c';
  if(sym=='+' || sym=='-' || sym=='/' || sym=='*'){
    input->op=sym;
    node * Node = CreateNode(input);
    push(Node);
    printf("$\n");
  }
}
int main(){
  int Q;
  scanf("%d",&Q);
  while (Q>0) {
    Q--;
    int typ;
    scanf("%d",&typ) ;
    if(typ==1){
      double no=0;
      scanf("%lf",&no);
      InsertNum(no);
    }
    else if(typ==2){
      char sym;
      scanf("%c",&sym);
      scanf("%c",&sym);
      InsertSymb(sym);
    }
    else if(typ==3){
      if(isEmpty(head)==1){
        printf("error\n");
      }
      else{
        PrintTop();
      }
    }
    else if(typ==4){
      if(isEmpty(head)==1){
        printf("True\n");
      }
      else{
        printf("False\n");
      }
    }
    else if(typ==5){
      if(isEmpty(head)==1){
        printf("error\n");
      }
      else{
        PrintTop();
        Pop();
      }
    }
  }
  while(isEmpty(head)==0){
    Pop();
  }
  return 0;
}
