/**
 * Date: 23.10.07
 * Number: LeetCode 92
 * Title: Reverse Linked List II
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
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    // number of 1 node
    if (!head.next) return head;

    var dummy = new ListNode(-1, head);
    var prev = dummy;

    // move prev node to left
    for (var i = 1; i < left; i++){
        prev = prev.next;
    }

    var crnt = prev.next;

    // reverse nodes
    for (var i = 0; i < right - left; i++){
        let nextNode = crnt.next;
        crnt.next = nextNode.next;
        nextNode.next = prev.next;
        prev.next = nextNode;
    }

    return dummy.next;
};