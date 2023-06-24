/**
 * Date: 23.06.24
 * Number: LeetCode 113
 * Title: Path Sum II
 * Level: Medium
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
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {
  var answer = []; //result
  
  function dfs(node, path, crntSum){
    //exit dfs funtion
    if(!node) return;

    //general case
    path.push(node.val);
    crntSum -= node.val;

    //currect targetSum
    if(!node.left && !node.right && crntSum === 0){
      answer.push(path.slice()); //append answer
      path.pop(); //undo selection
      return;
    }

    //call recursive method
    dfs(node.left, path, crntSum);
    dfs(node.right, path, crntSum);

    //undo selection
    path.pop();
  }

  //start backtracking
  dfs(root, [], targetSum);

  return answer;
};