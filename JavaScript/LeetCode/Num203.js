/**
 * Date: 23.09.13
 * Number: LeetCode 203
 * Title: Remove Linked List Elements
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
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    // create dummy node
    var dummyNode = new ListNode(-1);
    dummyNode.next = head;

    var crntNode = head; //current node
    var prevNode = dummyNode; // previous node

    while (crntNode){
        // remove element
        if (crntNode.val === val){
            prevNode.next = crntNode.next;
            crntNode = crntNode.next;
        }
        else { // move prevNode and crntNode
            prevNode = crntNode;
            crntNode = crntNode.next;
        }
    }

    return dummyNode.next;
};