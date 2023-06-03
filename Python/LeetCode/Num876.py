"""
Date:
  23.06.03
Number:
  LeetCode 876
Title:
  Middle of the Linked List
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
  def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    r = l = head #two pointers
    
    while l and l.next:
      r = r.next #move one step
      l = l.next.next #move two step
    
    #start r node for linked list
    return r