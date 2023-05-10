"""
Date:
  23.05.10
Number:
  LeetCode 1209
Title:
  Remove All Adjacent Duplicates in String II
Level:
  Medium
Name:
  thelight0804
"""

class Solution(object):
  def removeDuplicates(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    #stack = [[character, count]]
    stack = []
    
    for c in s:
      #add character count
      if stack and stack[-1][0] == c:
        stack[-1][1] += 1
        if stack[-1][1] == k: #pop
          stack.pop()
      #push first character
      else:
        stack.append([c, 1])
    
    #output stack to string
    return ''.join([c * count for c, count in stack])