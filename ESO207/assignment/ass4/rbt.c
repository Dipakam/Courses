#include<stdio.h>
#include<stdlib.h>
struct node {
  int key; // An integer less than 1000
  int colour; // 0 for red 1 for black
  struct node * parent;
  struct node * left;
  struct node * right;
};
typedef struct node node;
node * head = NULL;

node * CreateNode(int newkey){
  node * NewNode = NULL;
  NewNode = (node *)malloc(sizeof(node));
  NewNode -> parent = NULL;
  NewNode -> left = NULL;
  NewNode -> right = NULL;
  NewNode -> key = newkey;
  NewNode -> colour = 0; //New node is always going to be a red one
  return NewNode;
}

void DeleteNode (node * ToDelete){
  free ( ToDelete);
  return ;
}
void PrintNode(node * Node){
  node * father = Node -> parent;
  node * lchild = Node -> left;
  node * rchild = Node -> right;
  if(lchild == NULL){
    if(rchild == NULL){
      if(father == NULL){
        printf("%d (%d) (Leaf,father=Nope) - ",Node ->key,Node -> colour );
      }
      else{
        printf("%d (%d) (Leaf,father=%d) - ",Node ->key,Node -> colour,father->key );
      }
    }
    else{
      if(father == NULL){
        printf("%d (%d) (Right = %d,Father =NOpe)\n",Node -> key,Node -> colour,rchild -> key );
      }
      else{
        printf("%d (%d) (Right = %d,father = %d)\n",Node -> key,Node -> colour,rchild -> key,father->key );
      }
    }
  }
  else{
    if(rchild == NULL){
      if(father == NULL){
        printf("%d (%d) (Father = nope,Left = %d)\n",Node -> key,Node -> colour,lchild -> key );
      }
      else{
        printf("%d (%d) (Father = %d,Left = %d)\n",Node -> key,Node -> colour,father->key,lchild -> key );
      }
    }
    else{
      if(father != NULL){
        printf("%d (%d)(father = %d,left=%d,right = %d) -",Node -> key,Node->colour,father->key,lchild->key,rchild->key );
      }
      else{
        printf("%d (%d)(father = Nope,left=%d,right = %d) -",Node -> key,Node->colour,lchild->key,rchild->key );
      }
    }
  }
  return;
}
void PrintTree(node * root){
  if(root == NULL){
    return ;
  }
  else{
    PrintTree(root->left);
    PrintNode(root);
    PrintTree(root->right);
    return;
  }
}
void RotateClock(node * root){
  node * father = root -> parent;
  node * l = root -> left;
  node * r = root -> right;
  if(father == NULL){//Root node
    head = l;
    l -> parent = NULL;
  }
  else{
    if(father -> left == root){
      father -> left = l;
    }
    else{
      father -> right = l;
    }
    l -> parent = father ;
  }
  node * temp = l -> right;
  root -> left = temp;
  if(temp != NULL){
    temp -> parent = root;
  }
  l -> right = root;
  root -> parent = l;
  return;
}
//In clockwise l should be non null and in anticlock wise r should be non null
void RotateAntiClock(node * root){//Demands the middle node about which to rotate
  node * father = root -> parent;
  node * l = root -> left;
  node * r = root -> right;
  if(father == NULL){//Root node
    head = r;
    r -> parent = NULL;
  }
  else{
    if(father -> left == root){
      father -> left = r;
    }
    else{
      father -> right = r;
    }
    r -> parent = father ;
  }
  node * temp = r -> left;
  root -> right = temp;
  if(temp != NULL){
    temp -> parent = root;
  }
  r -> left = root;

  root -> parent = r;
  return;
}
void deleteLeafNodeFromTree(node * todel){
  node * father = todel -> parent;
  if(father == NULL){
    head = NULL;
    DeleteNode(todel);
    return;
  }
  if(father -> left == todel){
    father -> left = NULL;
  }
  else{
    father -> right = NULL;
  }
  DeleteNode(todel);
}
node * deleteOneChildNodeP(node * todel){//todel has only one child
  node * father = todel -> parent;
  node * child = NULL;
  //printf("Father has %d",father -> key );
  if(todel -> right == NULL){//Has a left child only
    child = todel -> left;
  }
  else{//Has a right child only
    child = todel -> right;
  }
  //printf("child has %d\n",child -> key );
  if(father != NULL && father -> left == todel ){
    father -> left = child ;
    child -> parent = father ;
    //printf("LEFT\n" );
  }
  else{
    if(father == NULL){
      head = child;
      child -> parent = NULL;
    }
    else{
      father -> right = child;
      child -> parent = father ;
    }
    //printf("RIGHT\n" );

  }

  DeleteNode(todel);
  //printf("CHild has %d\n",child -> key );
  return child ;
}
node * InsertBST(int newkey, node * root){
  node * curr=root;
  node * prev=NULL;
  int flag =0;
  node * NewNode = CreateNode(newkey);

  while(curr != NULL){
    prev = curr;
    if(curr->key > newkey){
      flag = 0;
      curr = curr->left;
    }
    else{
      flag = 1;
      curr = curr-> right;
    }
  }
  if(prev == NULL){
    head = NewNode;
    return head;
  }
  if(flag == 1){
    prev -> right = NewNode;
    NewNode -> parent = prev;
  }
  else{
    prev -> left = NewNode;
    NewNode -> parent = prev;
  }
  return NewNode;
}
int BlackHeight(node * root){
  int count = 0;
  node * curr = root;
  while(curr != NULL){
    count = count + curr->colour;
    curr = curr -> left;
  }
  return count;
}//Function returns the number of black nodes while traversing through the leftmost
//branch of the tree

void FixInsertRBT(node * Node){//Node is red node to be fixed
  if(Node == head){//Root node
    Node -> colour = 1;
    return;
  }
  else{//Not root node
    node * father = Node -> parent;
    if(father -> colour == 1){//Father is black and child is red
      return ; //No problem in this case
    }
    else{//Both father and child are red
      node * grandpa = father -> parent;
      if(grandpa == NULL){
        father -> colour = 1;
        return;
      }
      if(grandpa -> left == father){//father is left child
        node * uncle = grandpa -> right;
        if(uncle != NULL && uncle -> colour == 0){//uncle father child all red
          grandpa -> colour = 0;
          uncle -> colour = 1;
          father -> colour = 1;
          FixInsertRBT(grandpa);
          return;
        }
        else{//uncle is black
          if(father -> right == Node){//left-right case
            RotateAntiClock(father);
            FixInsertRBT(father);
            return;
          }
          else{//left - left case
            RotateClock(grandpa);
            father -> colour = 1;
            grandpa -> colour = 0;
            return;
          }
        }
      }
      else{//father is right child
        node * uncle = grandpa -> left;
        if(uncle != NULL && uncle -> colour == 0){//uncle father child all red
          grandpa -> colour = 0;
          uncle -> colour = 1;
          father -> colour = 1;
          FixInsertRBT(grandpa);
          return;
        }
        else{//uncle is black
          if(father -> left == Node){//right - left case
            RotateClock(father);
            FixInsertRBT(father);
            return;
          }
          else{//right-right case
            RotateAntiClock(grandpa);
            grandpa -> colour = 0;
            father -> colour = 1;
            return;
          }
        }
      }
    }
  }
}
node * SearchKey(node * root,int searchkey){
  if(root == NULL){
    return NULL;
  }
  if(root -> key == searchkey){
    return root;
  }
  else{
    if(root -> key > searchkey){
      return SearchKey(root->left,searchkey);
    }
    else{
      return SearchKey(root->right,searchkey);
    }
  }
}//This function returns the pointer the node which contains the given key
//In case it does not find the given key it returns NULL pointer
node * succesor(node * test){
  //We are calling the succesor function only when the given node has both of children
  //It means that the given node test has both the children present
  node * succ = test;
  succ = succ -> right;//which exists and we assume that
  while (succ -> left != NULL ){
    succ = succ -> left;
  }
  return succ ;
}//Succ is going to be a leaf node
//In this case we know that the given node has two children and in that perticuar
//case only we have to calculate the succesor so just go right and then left
//The output can have a right child but not the left child

void FixDoubleBlack(node * father){//Takes input as father of double black
  if(father == NULL){
    if(head == NULL){
      return;
    }
    head -> colour = 1;//make double black a single black
    return ;
  }
  else{
    node * lchild = father -> left;
    node * rchild = father -> right;
    node * dblack = NULL;
    if(lchild == NULL || lchild -> colour == 2){//left child is double black
      dblack = lchild;
      node * sibling = rchild ; //sibling is right child
      if(sibling -> colour == 1){//sibling is black
        lchild = sibling -> left;
        rchild = sibling -> right;
        if(lchild != NULL && lchild -> colour == 0){//left child of sibling is red
          if(rchild != NULL && rchild -> colour == 0){//both children of sibling are red
            //PrintTree(head);
            RotateAntiClock(father);
            //PrintTree(head);
            rchild -> colour = father -> colour;
            if(dblack != NULL){
              dblack -> colour = 1;
            }
            return;
          }
          else{//right is black left is red
            //PrintTree(head);
            RotateClock(sibling);
            //PrintTree(head);
            RotateAntiClock(father);
            //PrintTree(head);
            lchild -> colour = father -> colour;
            father -> colour = 1;
            if(dblack != NULL){
              dblack -> colour = 1;
            }
            return;
          }
        }
        else{//left child of sibling is black
          if(rchild != NULL && rchild -> colour == 0){//left black and right red
            //PrintTree(head);
            RotateAntiClock(father);
            //PrintTree(head);
            rchild -> colour = father -> colour;
            if(dblack != NULL){
              dblack -> colour = 1;
            }
            return;
          }
          else{//Both children of sibling  are black
            if(dblack != NULL){
              dblack -> colour = 1;
            }
            sibling -> colour = 0;
            father -> colour++;
            node * grandpa = father -> parent;
            if(father -> colour == 2){
              //PrintTree(head);
              FixDoubleBlack(grandpa);
              //PrintTree(head);
            }
            return;
          }
        }

      }
      else{//silbling is red
        //PrintTree(head);
        RotateAntiClock(father);
        sibling -> colour = father -> colour;
        father -> colour = 0;
        FixDoubleBlack(father);
        //PrintTree(head);
        return;
      }
    }
    else{//right child is double black
      dblack = rchild ;
      node * sibling = lchild;//sibling is left child
      lchild = sibling -> left;
      rchild = sibling -> right;
      if(sibling -> colour == 1){//sibling is black
        lchild = sibling -> left;
        rchild = sibling -> right;
        if(lchild != NULL && lchild -> colour == 0){//left child of sibling is red
          if(rchild != NULL && rchild -> colour == 0){//both children of sibling are red
            //PrintTree(head);
            RotateClock(father);
            //PrintTree(head);
            lchild -> colour = father -> colour;
            if(dblack != NULL){
              dblack -> colour = 1;
            }
            return;
          }
          else{//right is black left is red
            //PrintTree(head);
            RotateClock(father);
            //PrintTree(head);
            lchild -> colour = father -> colour;
            if(dblack != NULL){
              dblack -> colour = 1;
            }
            return;
          }
        }
        else{//left child of sibling is black
          if(rchild != NULL && rchild -> colour == 0){//left black and right red
            //PrintTree(head);
            RotateAntiClock(sibling);
            //PrintTree(head);
            RotateClock(father);
            //PrintTree(head);
            rchild -> colour = father -> colour;
            father -> colour = 1;
            if(dblack != NULL){
              dblack -> colour = 1;
            }
            return;
          }
          else{//Both children of sibling  are black
            if(dblack != NULL){
              dblack -> colour = 1;
            }
            sibling -> colour = 0;
            father -> colour++;
            node * grandpa = father -> parent;
            if(father -> colour == 2){
              //PrintTree(head);
              FixDoubleBlack(grandpa);
              //PrintTree(head);
            }
            return;
          }
        }

      }
      else{//silbling is red
        //PrintTree(head);
        RotateClock(father);
        //PrintTree(head);
        sibling -> colour = father -> colour;
        father -> colour = 0;
        FixDoubleBlack(father);
        //PrintTree(head);
        return;
      }
    }
  }
}

void Transplant (node* u, node*v){
  if (u->parent == NULL)
    head = v;
  else if (u == u->parent->left)
    u->parent->left = v;
  else
    u->parent->right = v;
  v->parent = u->parent;
}


void DeleteLeafOrOneChild(node * todel){//either a leaf or a child
  if(todel -> right == NULL){//No right child
    if(todel -> left == NULL){//Leaf node
      node * father = todel -> parent;
      int color = todel -> colour ;
      //DeleteNode(todel);
      deleteLeafNodeFromTree(todel);
      color++;
      if(color == 2){
        FixDoubleBlack(father);
      }
      //printf("I got here" );
      return ;
    }
    else{//Only left child
      node * father = todel -> parent;
      int color = todel -> colour;
      node * newChildNode = deleteOneChildNodeP(todel);
      newChildNode -> colour += color ;
      color = newChildNode -> colour;
      if(color == 2){
        FixDoubleBlack(father);
      }
      return;
    }
  }
  else{//A right child
    node * father = todel -> parent;
    int color = todel -> colour;
    //PrintTree(head);
    //printf("Check Here before\n" );
    //printf("Todel has %d\n",todel -> key );
    //printf("Father of todel has %d\n",father -> key );
    //printf("Head has right as %d\n",(head -> right)->key );
    node * newChildNode = deleteOneChildNodeP(todel);
    //PrintTree(head);
    //printf("Check Here\n" );
    newChildNode -> colour += color ;
    color = newChildNode -> colour;
    if(color == 2){
      FixDoubleBlack(father);
    }
    return;
  }
}

void DeleteKey(node * root,int deletekey){
  //printf("deletekey = %d\n",deletekey );
  node * todel = SearchKey(root,deletekey);
  if(todel == NULL){
    printf("-1");
    return;
  }
  else{//We need to check if it is leaf node
    //printf("Not null branch\n" );
    if(todel -> right == NULL){//It does not have a right child
      if(todel -> left == NULL){//It is a leaf node
        DeleteLeafOrOneChild(todel);
        printf("%d",BlackHeight(head));
      }
      else{// It only has a left child
        DeleteLeafOrOneChild(todel);
        printf("%d",BlackHeight(head));
      }
    }
    else{//It has a right child
      //printf("Has a right child branch\n" );
      if(todel -> left == NULL){//It only has a right child
        DeleteLeafOrOneChild(todel);
        printf("%d",BlackHeight(head));
      }
      else{//It has both the children
        //printf("Has both children\n" );
        node * succ = succesor (todel);
        //printf("succesor has %d\n",succ -> key );
        todel -> key = succ -> key;
        node * father = todel -> parent;
        node * fatherofsucc = succ -> parent;
        //printf("father of todel= %d is %d\n",todel -> key,father -> key );
        node * child = todel -> left;
        //printf("Child of todel has parent = %d \n",(child -> parent)->key );
        //printf("Dather of succ = %d is %d \n",succ -> key ,fatherofsucc -> key );
        DeleteLeafOrOneChild(succ);
        //printf("father of todel= %d is %d\n",todel -> key,father -> key );
        //printf("Dather of succ = %d is %d \n",succ -> key ,fatherofsucc -> key );
        //printf("Child of todel has parent = %d \n",(child -> parent)->key );
        printf("%d",BlackHeight(head));
      }
    }
  }
}
void DeleteTree(node * root){
  if(root == NULL){
    return ;
  }
  else{
    DeleteTree(root -> left);
    DeleteTree(root -> right);
    DeleteNode(root);
  }
}
//
int main(){
  int n1;
  scanf("%d\n",&n1 );
  int key;
  node * alpha;
  for(int i=0;i<n1;i++){
    scanf("%d", &key);
    if(SearchKey(head,key) == NULL){
      alpha = InsertBST(key,head);
      FixInsertRBT(alpha);
    }
    printf("%d ",BlackHeight(head));
    //PrintTree(head);
    //printf("\nInsertion of key = %d\n",key );
    //printf("%d\n",alpha -> key );
  }
  //PrintTree(head);
  printf("\n");
int n2;
  scanf("%d\n",&n2 );
  for(int i=0 ; i< n2;i++){
    scanf("%d", &key);
    DeleteKey(head,key);
    /*alpha = SearchKey(head,key);
    if(alpha == NULL){
      printf("-1" );
    }
    else{
      CLRSdelete(alpha);
      printf("%d",BlackHeight(head));
      //printf("%d", BlackHeight());
    }*/
    printf(" ");
    PrintTree(head);
    printf("Deletion of %d done\n",key);

  }
  printf("\n");
  int n3;
  scanf("%d\n",&n3);
  for(int i=0 ; i< n3 ; i++){
    scanf("%d", &key);
    alpha = SearchKey(head,key);
    if(alpha == NULL){
      printf("-1,-1 ");
    }
    else{
      if(alpha -> colour == 0){
        printf("r," );
      }
      else{
        printf("b,");
      }
      printf("%d ",BlackHeight(alpha) );
    }
  }
  printf("\n");

  //PrintTree(head);
  DeleteTree(head);
  return 0;
}
