#include<stdio.h>

struct node {
  struct node * front;
  struct node * back;
  int Type;//0 for literal ,1 for and ,2 for or ,3 for not
  int proposition;//only if Type=0
};

int main(){
  struct node * head 
}
