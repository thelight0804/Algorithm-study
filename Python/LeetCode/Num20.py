"""
Date:
  23.05.06
Number:
  LeetCode 20
Title:
  Valid Parentheses
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = [] #parentheses stack
    for i in s:
      if i in '([{':
        stack.append(i)
      else:
        if not stack:
          return False
        elif i == ')' and stack[-1] == '(':
          stack.pop()
        elif i == ']' and stack[-1] == '[':
          stack.pop()
        elif i == '}' and stack[-1] == '{':
          stack.pop()
        else:
          return False
    
    if not stack: return True
    else:return False