/**
 * Date: 23.10.19
 * Number: LeetCode 21
 * Title: Merge Two Sorted Lists
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
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    // empty list1 or list 2
    if (!list1) return list2;
    else if (!list2) return list1;

    // create new merge list
    var list = new ListNode(-1, null);
    var crnt = list; //set current node of new merge list

    // iterate lists
    while (list1 && list2){
        // crnt.next link to list 1
        if (list1.val < list2.val){
            crnt.next = list1;
            list1 = list1.next;
        }
        // crnt.next link to list 2
        else {
            crnt.next = list2;
            list2 = list2.next;
        }
        // move crnt node to next
        crnt = crnt.next;
    }

    // link last nodes in list
    crnt.next = list1 || list2;
    
    // return merged list
    return list.next;
};