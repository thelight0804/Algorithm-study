"""
Date:
  23.06.18
Number:
  LeetCode 292
Title:
   Nim Game
Level:
  Easy
Author:
  thelight0804
"""

class Solution(object):
  def canWinNim(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 4: return True
    else: return n % 4 != 0