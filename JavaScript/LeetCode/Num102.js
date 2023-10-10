/**
 * Date: 23.10.08
 * Number: LeetCode 102
 * Title: Binary Tree Level Order Traversal
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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    // empty tree
    if (!root) return [];

    var tree = [];
    
    var queue = []; // tree node queue of level
    queue.push(root);

    while (queue.length > 0){
        var count = queue.length;
        var levels = []; // push node of current level

        for (var i = 0; i < count; i++){
            // get next node
            var crntNode = queue.shift();
            // push node of current level
            levels.push(crntNode.val)

            // push sub node in queue
            if (crntNode.left){
                queue.push(crntNode.left);
            }
            if (crntNode.right){
                queue.push(crntNode.right);
            }
        }

        // push nodes arrya of current level
        tree.push(levels);
    }
    
    return tree;
};