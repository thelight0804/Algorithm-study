/**
 * Date: 23.09.22
 * Number: LeetCode 19
 * Title: Remove Nth Node From End of List
 * Level: Medium
 * Author: thelight0804
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    var left = head;
    var right = head;

    // move right node
    for (var i = 0; i < n; i++){
        right = right.next;
    }

    // n is equal length of linked list
    if (!right) return head.next;

    // move right and left node
    while (right.next){
        right = right.next;
        left = left.next;
    }

    // remove n node
    left.next = left.next.next;

    return head;
};