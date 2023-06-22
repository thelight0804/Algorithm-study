/*
Date:
  2023.06.22
Title:
  Traverse tree iterative
Author:
  thelight0804
*/

//create node class
class Node{
  constructor(val){
    this.val = val;
    this.left = null;
    this.right = null;
  }
}


//create node
node1 = new Node(1);
node2 = new Node(2);
node3 = new Node(3);
node4 = new Node(4);
node5 = new Node(5);
node6 = new Node(6);
node7 = new Node(7);

//make tree by link nodes
node1.left = node2;
node1.right = node3;
node2.left = node4;
node2.right = node5;
node3.left = node6;
node3.right = node7;


//preOrder - NLR
console.group('preOrder')
function preOrder(node){
  if(!node) return; //exit funciton

  var stack = []; //create nodes stack
  stack.push(node); //push root node

  while(stack.length > 0){
    //pop node
    crntNode = stack.pop();
    console.log(crntNode.val);

    //push node
    if(crntNode.right)
      stack.push(crntNode.right);
    if(crntNode.left)
      stack.push(crntNode.left);
  }
}
preOrder(node1); //1 2 4 5 3 6 7
console.groupEnd('preOrder')


//inOrder - LNR
console.group('InOrder')
function inOrder(node){
  if(!node) return;
  var stack = []; //create nodes stack
  crntNode = node; //set crntNode to root node

  while(true){
    //push left node
    if(crntNode){
      stack.push(crntNode);
      crntNode = crntNode.left;
    }
    //left node is null
    else if(stack.length > 0){
      crntNode = stack.pop();
      console.log(crntNode.val);
      crntNode = crntNode.right;
    }
    //crntNode is null
    else
      break;
  }
}
inOrder(node1); //4 2 5 1 6 3 7
console.groupEnd('InOrder')


//postOrder - LRN
console.group('postOrder')
function postOrder(node){
  if(!node) return;
  var stack = []; //create nodes stack

  var crntNode = node; //set crntNode to root node
  var lastNode = null; //last print node

  while(true){
    //push left nodes
    if(crntNode){
      stack.push(crntNode);
      crntNode = crntNode.left;
    }
    //left node is null
    else if(stack.length > 0){
      peekNode = stack.pop();
      if(peekNode.right && peekNode.right != lastNode){ //check right node
        stack.push(peekNode);
        crntNode = peekNode.right;
      }
      else{ //not exist right node
        console.log(peekNode.val);
        lastNode = peekNode;
      }
    }
    else //crntNode is null
      break;
  }
}
postOrder(node1);
console.groupEnd('postOrder')