/*
Date:
  2023.06.21
Title:
  Tree level Order
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

console.group("treeLevelPrint");
function treeLevelPrint(node){
  if(node === null) return

  var queue = [];
  queue.push(node); //push root node

  while(queue.length > 0){
    crntNode = queue.shift(); //pop node
    console.log(crntNode.val); //print value
    
    if(crntNode.left){ //push left node
      queue.push(crntNode.left);
    }
      
    if(crntNode.right){ //push right node
      queue.push(crntNode.right);
    }
  }
}
treeLevelPrint(node1); //1 2 3 4 5 6 7
console.groupEnd("treeLevelPrint");

console.group("treeLevelNewLinePrint");
function treeLevelNewLinePrint(node){
  if(!node) return;

  var queue = [];
  queue.push(node);

  while(queue.length > 0){
    var count = queue.length; //set count
    for(var i = 0; i < count; i++){
      //print count
      crntNode = queue.shift();
      console.log(crntNode.val);
      if(crntNode.left)
        queue.push(crntNode.left);
      if(crntNode.right)
        queue.push(crntNode.right);
    }
    console.log("----"); //new line
  }
}
treeLevelNewLinePrint(node1);
console.groupEnd("treeLevelNewLinePrint");
/*
1
----
2
3
----
4
5
6
7
----
*/
