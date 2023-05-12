"""
Date:
  23.05.12
Number:
  LeetCode 242
Title:
  Valid Anagram
Level:
  Easy
Name:
  thelight0804
"""

#### use hash table
class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    table = {}

    # add character count of c
    for c in s:
      if table.get(c) is None:
        table[c] = 1
      else:
        table[c] += 1
    
    # sub character count of t
    for c in t:
      #not exist character
      if table.get(c) is None:
        return False
      else:
        table[c] -= 1
        #not match character count
        if table[c] < 0: return False
    
    #not match character count
    for i in table.values():
      if i != 0: return False
    
    #match anagram
    return True

#### use sort
class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t): return False
    elif sorted(s) != sorted(t): return False
    else: return True