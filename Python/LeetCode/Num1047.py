"""
Date:
  23.05.09
Number:
  LeetCode 1047
Title:
  Remove All Adjacent Duplicates In String
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def removeDuplicates(self, s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    
    for c in s:
      #not equal character
      if not stack or stack[-1] != c:
        stack.append(c)
      else: #equal character
        stack.pop()
    
    return ''.join(stack)