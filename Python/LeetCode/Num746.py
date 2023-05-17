"""
Date:
  23.05.17
Number:
  LeetCode 746
Title:
  Min Cost Climbing Stairs
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    #memoization of need pay cost
    f = [0] * (len(cost) + 1)
    
    for i in range(len(cost) + 1):
      #fixed values
      if i == 0 or i == 1:
        f[i] = 0
      else: #dynamic programming
        f[i] = min(f[i-2] + cost[i-2], f[i-1] + cost[i-1])

    #return result
    return f[-1]