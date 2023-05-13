"""
Date:
  23.05.13
Number:
  LeetCode 290
Title:
  Word Pattern
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def wordPattern(self, pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    #string to array
    s = s.split()
    table = {} #hashmap table

    #not match count
    if len(pattern) != len(s): return False

    for i , c in enumerate(pattern):
      #add key, value
      if table.get(c) is None:
        table[c] = s[i]
      
      #not match
      if table.get(c) != s[i] or len(table.values()) != len(set(table.values())):
        return False

    return True