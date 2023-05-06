"""
Date:
  23.05.06
Number:
  LeetCode 1249
Title:
  Minimum Remove to Make Valid Parentheses
Level:
  Medium
Name:
  thelight0804
"""

class Solution(object):
  def minRemoveToMakeValid(self, s):
    """
    :type s: str
    :rtype: str
    """
    l = list(s) #string to list 1
    stack = [] #parentheses index stack

    for i in range(len(s)):
      if s[i] == '(': #2
        stack.append(i) #push '(' index
      elif s[i] == ')': #3
        if stack: #a
          stack.pop()
        else: #b
          l[i] = '' #remove ')'
    
    #remove '(' to use index 4
    for i in stack:
      l[i] = ''

    #output list to join string 5
    return ''.join(l)