#include<stdio.h>
#include<stdlib.h>
#include<string.h>
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
  //printf("$\n");
}
void InsertSymb(char sym){
  numop * input = CreateStack();
  input = (numop *)malloc(sizeof(numop));
  input->type = 'c';
  if(sym=='+' || sym=='-' || sym=='/' || sym=='*'){
    input->op=sym;
    node * Node = CreateNode(input);
    push(Node);
    //printf("$\n");
  }
}
void PrintStack(){
  node * curr = head;
  while(curr){
    if((curr->item)->type=='n'){
      printf("%lf\n",(curr->item)->num );
    }
    else{
      printf("%c\n",(curr->item)->op );
    }
    curr = curr->next;
  }
  return;
}
double Evaluate(){
  //printf("The stack looks like this: \n");
  //PrintStack();
  if((Top()->type)=='n'){
    double number = Top()->num;
    Pop();
    return number;
  }
  else{
    if((Top()->op)=='+'){
      Pop();
      double num1 = Evaluate();
      double num2 = Evaluate();
      return num1+num2;
    }
    else if((Top()->op)=='-'){
      Pop();
      double num1 = Evaluate();
      double num2 = Evaluate();
      return num1-num2;
    }
    else if((Top()->op)=='*'){
      Pop();
      double num1 = Evaluate();
      double num2 = Evaluate();
      return num1*num2;
    }
    else if((Top()->op)=='/'){
      Pop();
      double num1 = Evaluate();
      double num2 = Evaluate();
      return num1/num2;
    }
  }
}
int main(){

  char s1[1000],s[1000];
  fgets(s1,1000,stdin);
  int count = 0,begin,end=0;
  while (s1[count] != '\0')
      count++;

   end = count - 1;

   for (begin = 0; begin < count; begin++) {
      s[begin] = s1[end];
      end--;
   }

   s[begin] = '\0';

  //printf("%s\n",s );
  int i=0;
  while (s[i]) {
    if(s[i]=='+'||s[i]=='*'||s[i]=='-'||s[i]=='/'){
      InsertSymb(s[i]);
      //PrintTop();
    }
    /*else if(s[i]==' '){
      continue;
    }*/
    else{
      if(s[i]>='0' && s[i]<= '9'){
        s[i]=s[i]+1-'1';
        //printf("It was here\n" );
        InsertNum(s[i]);
        //PrintTop();
      }
    }
    i++;
  }
  //PrintStack();
  printf("%lf\n",Evaluate() );
  while(isEmpty(head)==0){
    //printf("tried to print\n");
    PrintTop();
    Pop();
  }
  //printf("%d\n",Evaluate());
  return 0;
}
