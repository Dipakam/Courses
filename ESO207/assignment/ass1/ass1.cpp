#include<iostream>
using namespace std;
struct numop{
  char type;
  char op;
  int num;
};

typedef struct numop numop;
struct node{
  numop * item;
  struct node * next;
};
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
  delete key->item;
  delete key;
  return;
}
void Pop(){
  node * clear=head;
  head = clear->next;
  deleteNode (clear);
  return;
}
typedef struct node node;
numop * CreateStack(){
  numop * pointer=NULL;
  //pointer = new numop;
  return pointer;
}
node * CreateNode(numop * key){
  node * Node = NULL;
  Node = new node;
  Node->item = key;
  Node->next = NULL;
  return Node;
}

int main(){
  /*numop test;
  test.type ='n';
  test.num = 4;*/
  /*numop * test = CreateStack();
  if(test==NULL){
    std::/* message cout << "ok" << '\n';
  }*/
  /*node * testnode=NULL;
  testnode = new node;
  testnode->next = NULL;
  testnode->item = &test;
  push(testnode);
  Pop();*/
  //delete test;

  //std::cout << (head->item)->num << '\n';
  //delete testnode;
  //std::cout << isEmpty(head) << '\n';
  int Q;
  std::cin >> Q;
  while (Q>0) {
    Q--;
    char typ;
    std::cin >>typ ;
    if(typ=='1'){
      int no=0;
      std::cin >> no;
      numop * input=CreateStack();
      input = new numop;
      input->type = 'n';
      input->num = no;
      node * Node = CreateNode(input);
      push(Node);
      std::cout << "$" << '\n';
    }
    else if(typ=='2'){
      char sym;
      //std::cin >> sym;
      std::cin >> sym;
      numop * input = CreateStack();
      input = new numop;
      input->type = 'c';
      if(sym=='+' || sym=='-' || sym=='/' || sym=='*'){
        input->op=sym;
        node * Node = CreateNode(input);
        push(Node);
        std::cout << "$" << '\n';
      }
    }
    else if(typ=='3'){
      if(isEmpty(head)==1){
        std::cout << "error" << '\n';
      }
      else{

      }
    }
  }
  while(isEmpty(head)==0){
    Pop();
  }
  return 0;
}
