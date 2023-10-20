/**
 * Date: 23.10.20
 * Number: LeetCode 108
 * Title: Convert Sorted Array to Binary Search Tree
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
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    // start recursive Function
    return preOlder(nums);
};

function preOlder(nums){
    // set null node
    if (nums.length === 0) return null;

    // get middle value
    var mid = Math.floor(nums.length / 2);
    // create node
    var node = new TreeNode(nums[mid]);
    
    // set left and right node
    node.left = preOlder(nums.slice(0, mid));
    node.right = preOlder(nums.slice(mid + 1));

    // return height-balanced binary tree
    return node;
}