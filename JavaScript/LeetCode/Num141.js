/**
 * Date: 23.11.05
 * Number: LeetCode 141
 * Title: Linked List Cycle
 * Level: Easy
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
 * @param {ListNode} head
 * @return {boolean}
 */

// Use recursive function
var hasCycle = function(head) {
    // create set object
    var set = new Set();

    // recursive function
    function traverse(node){
        // check linked list cycle
        // also, this is end condition of recursive function
        if (!node) return false;
        if (set.has(node)) return true;

        // add node in set object
        set.add(node);

        // call next recursive function
        return traverse(node.next);
    }

    // call first recursive function
    return traverse(head);
};


// Use two pointer
var hasCycle = function(head) {
    // initialize two pointers
    var slow = head;
    var fast = head;

    // move two pointers
    while (fast && fast.next){
        slow = slow.next;
        fast = fast.next.next;

        // check linked list cycle
        if (fast === slow) return true;
    }

    // not linked list cycle
    return false;
};
