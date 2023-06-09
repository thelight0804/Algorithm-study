"""
Date:
  23.06.09
Number:
  LeetCode 1863
Title:
   Sum of All Subset XOR Totals
Level:
  Easy
Author:
  thelight0804
"""

class Solution(object):
  def subsetXORSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    self.total = 0 #XOR total

    def dfs(subset, start):
      xorSum = 0 #sum XOR in subset
      for n in subset:
        xorSum = xorSum ^ n
      self.total += xorSum #add XOR total
      print(subset, xorSum, self.total)
      
      #exclude old numbers in a for statement starting at start
      for i in range(start, len(nums)):
        subset.append(nums[i])
        dfs(subset, i+1) #backtracking
        subset.pop()

    dfs([], 0) #start backtraking

    return self.total