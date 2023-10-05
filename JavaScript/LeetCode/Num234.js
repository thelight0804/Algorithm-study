/**
 * Date: 23.10.05
 * Number: LeetCode 234
 * Title: Palindrome Linked List
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
 * @return {boolean}
 */
var isPalindrome = function(head) {
    var left = head;

    function palindrome(right){
        if (!right){
            return true;
        }

        // travel last node
        var rightSame = palindrome(right.next);

        // compare left node and right node
        var leftSame = left.val === right.val;

        // move left node
        left = left.next;

        // check palindrome 
        return leftSame && rightSame;
    }

    return palindrome(head);
};