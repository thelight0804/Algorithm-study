"""
Date:
  23.06.15
Number:
  LeetCode 21
Title:
   Merge Two Sorted Lists
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
  def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    #exception empty list
    if list1 is None: return list2
    if list2 is None: return list1
    
    #add dummyNode
    dummyNode = ListNode(-1)
    crntNode = dummyNode

    node1 = list1
    node2 = list2

    #merge two lists
    while node1 and node2:
      if node1.val <= node2.val:
        crntNode.next = node1 #crntNode link next node
        node1 = node1.next #node1 move next
        crntNode = crntNode.next #crntNode move next
      else:
        crntNode.next = node2
        node2 = node2.next
        crntNode = crntNode.next
    
    #link remain node link
    if node1:
      crntNode.next = node1
    else:
      crntNode.next = node2

    return dummyNode.next