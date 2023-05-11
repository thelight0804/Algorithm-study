"""
Date:
  23.05.11
Number:
  LeetCode 205
Title:
  Isomorphic Strings
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    #create two hast talbe
    table1 = {}
    table2 = {}

    for i in range(len(s)):
      #get value
      char1 = table1.get(s[i])
      char2 = table2.get(t[i])

      #None value
      if char1 is None and char2 is None:
        table1[s[i]] = t[i]
        table2[t[i]] = s[i]
      #dismatch value
      elif char1 != t[i] or char2 != s[i]:
        return False

    #match
    return True