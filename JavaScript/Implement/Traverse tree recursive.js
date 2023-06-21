/*
Date:
  2023.06.21
Number:
  LeetCode 232
Title:
  Traverse tree recursive
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
  if(node === null) return; //exit funciton
  console.log(node.val); //print node
  preOrder(node.left); //call recursive funtion left
  preOrder(node.right); //call recursive funtion right
}
preOrder(node1); //1 2 4 5 3 6 7
console.groupEnd('preOrder')


//inOrder - LNR
console.group('InOrder')
function inOrder(node){
  if(node === null) return; //exit funciton
  inOrder(node.left); //call recursive funtion left
  console.log(node.val); //print node
  inOrder(node.right); //call recursive funtion right
}
inOrder(node1); //4 2 5 1 6 3 7
console.groupEnd('InOrder')


//postOrder - LRN
console.group('postOrder')
function postOrder(node){
  if(node === null) return; //exit funciton
  postOrder(node.left); //call recursive funtion left
  postOrder(node.right); //call recursive funtion right
  console.log(node.val); //print node
}
postOrder(node1);
console.groupEnd('postOrder')