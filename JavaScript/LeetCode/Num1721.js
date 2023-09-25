/**
 * Date: 23.09.22
 * Number: LeetCode 1721
 * Title: Swapping Nodes in a Linked List
 * Level: Medium
 * Author: thelight0804
 */

// use two pointers
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function(head, k) {
    // initialize two pointers
    var left = head;
    var right = head;

    // move left to k
    for (var i = 1; i < k; i++){
        left = left.next;
    }
    // get left node
    var crnt = left;

    // move right to end of k
    while (crnt.next){
        crnt = crnt.next;
        right = right.next;
    }

    // swap two values
    var tmp = left.val;
    left.val = right.val;
    right.val = tmp;

    return head;
};

// use array
var swapNodes = function(head, k) {
    var node = head;
    var arr = [];

    // append node value in array
    while (node){
        arr.push(node.val);
        node = node.next;
    }

    // swap two values
    var tmp = arr[k - 1];
    arr[k - 1] = arr[arr.length - k];
    arr[arr.length - k] = tmp;

    // convert swaped array to linked list
    node = head;
    for (var i = 0; i < arr.length; i++){
        node.val = arr[i];
        node = node.next;
    }
    
    return head;
};