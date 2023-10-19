/**
 * Date: 23.10.19
 * Number: LeetCode 148
 * Title: Sort List
 * Level: Medium
 * Author: thelight0804
 */

// use recursive
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
var sortList = function(head) {
    // start recursive function
    var sortedList = split(head);
    return sortedList;
};

// split middle of linked list
function split(head){
    // get one node of split linked list
    if (!head || !head.next){
        return head;
    }

    // get middle value in linked list
    // use slow & fast two pointer
    var slow = head;
    var fast = head.next;

    while (fast && fast.next){
        slow = slow.next;
        fast = fast.next.next
    }
    var mid = slow.next;

    // split left and right
    slow.next = null;

    // recursive function to middle split
    var left = sortList(head);
    var right = sortList(mid);

    // merge linked list
    return merge(left, right);
}

function merge(left, right){
    // create new linked list
    var dummy = new ListNode(0);
    var crnt = dummy;

    // link next node in ascending order
    while (left && right){
        if (left.val <= right.val){
            crnt.next = left;
            left = left.next
        }
        else {
            crnt.next = right;
            right = right.next;
        }
        crnt = crnt.next;
    }

    // link last node
    if (left) crnt.next = left;
    else if (right) crnt.next = right;

    return dummy.next;
}


// use array
var sortList = function(head) {
    // node values array
    var arr = [];

    // get node values into array
    while(head){
        arr.push(head.val);
        head = head.next;
    }

    // sort array
    arr.sort((a, b) => a - b);

    // create sort list
    var sortList = new ListNode(-1);
    var crnt = sortList;

    // array to linked list
    for (var n of arr){
        crnt.next = new ListNode(n);
        crnt = crnt.next;
    }

    // return sorted list
    return sortList.next;
};