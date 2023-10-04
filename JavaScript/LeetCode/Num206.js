/**
 * Date: 23.10.04
 * Number: LeetCode 206
 * Title: Reverse Linked List
 * Level: Easy
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
 * @return {ListNode}
 */
var reverseList = function(head) {
    // nothing linked list
    if (!head) return head;

    // recursive funtion
    function reverse(head, prev){
        // end node of linked list
        if (!head) return prev;

        // move next
        var next = head.next;
        // head.next link before node
        head.next = prev;

        // move next node
        return reverse(next, head);
    }

    // call recursive funtion
    return reverse(head, null);
};