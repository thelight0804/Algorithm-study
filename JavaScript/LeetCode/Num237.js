/**
 * Date: 23.09.12
 * Number: LeetCode 237
 * Title: Delete Node in a Linked List
 * Level: Medium
 * Author: thelight0804
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function(node) {
    node.val = node.next.val; // copy next node
    node.next = node.next.next; // update current node.next pointer with next node.next
};