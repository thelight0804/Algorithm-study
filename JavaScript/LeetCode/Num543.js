/**
 * Date: 23.06.28
 * Number: LeetCode 543
 * Title: Diameter of Binary Tree
 * Level: Easy
 * Author: thelight0804
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
  var max = 0; //max length

  function dfs(node){
    if(!node) return 0; //not exist node
    
    var left = dfs(node.left); //left depth
    var right = dfs(node.right); //right depth

    max = Math.max(max, left + right); //get max length
    depth = Math.max(left, right); //get max depth

    return depth + 1; //back root so add 1
  }

  //start tree traversal
  dfs(root);
  return max;
};