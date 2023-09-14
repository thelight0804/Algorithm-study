/**
 * Date: 23.09.14
 * Number: LeetCode 104
 * Title: Maximum Depth of Binary Tree
 * Level: Easy
 * Author: thelight0804
 */

// iterative
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
var maxDepth = function(root) {
    if (!root) return 0;

    var depth = 0; // maximum depth count
    var queue = [root];

    while (queue.length > 0){
        var count = queue.length; // node count of level
        for (var i = 0; i < count; i++){
            var crnt = queue.shift();
            if (crnt.left) queue.push(crnt.left);
            if (crnt.right) queue.push(crnt.right);
        }
        depth ++; // add depth count
    }
    
    return depth;
};

// recursive
var maxDepth = function(root) {
    if (!root) return 0;

    // call recursive funtion
    var left = maxDepth(root.left);
    var right = maxDepth(root.right);
    
    // maximum of two depth add 1
    return Math.max(left, right) + 1;
};