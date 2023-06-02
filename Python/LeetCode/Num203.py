"""
Date:
  23.06.02
Number:
  LeetCode 203
Title:
  Remove Linked List Elements
Level:
  Easy
Author:
  thelight0804
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
  def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    dummyNode = ListNode(-1) #create dummy node
    dummyNode.next = head #link nodes

    crntNode = head #current node
    prevNode = dummyNode #previous node

    while crntNode:
      if crntNode.val == val: #equal value
        prevNode.next = crntNode.next #link next node
        crntNode = crntNode.next #move crntNode
      else:
        crntNode = crntNode.next #move crntNode
        prevNode = prevNode.next #move prevNode
    
    return dummyNode.next
    