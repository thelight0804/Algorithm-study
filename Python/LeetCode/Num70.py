"""
Date:
  23.05.17
Number:
  LeetCode 70
Title:
  Climbing Stairs
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    #memoization
    f = [0 for i in range(n+1)]
    for i in range(1, n+1):
      if i == 1: f[1] = 1
      elif i == 2: f[2] = 2
      else: #dynamic algorithm
        f[i] = f[i-1] + f[i-2]

    #return output
    return f[-1]