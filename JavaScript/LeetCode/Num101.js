/**
 * Date: 23.10.06
 * Number: LeetCode 101
 * Title: Symmetric Tree
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
 * @return {boolean}
 */
var isSymmetric = function(root) {
    // treval tree
    return isSame(root.left, root.right);
};

function isSame(left, right){
    // end of tree
    if (!left || !right){
        return left === right;
    }

    // check both values
    if (left.val === right.val){
        // go to sub trees
        return isSame(left.left, right.right) && isSame(left.right, right.left);
    }
    else {
        // incorrect values
        return false;
    }
}
