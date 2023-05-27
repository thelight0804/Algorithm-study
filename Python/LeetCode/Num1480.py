"""
Date:
  23.05.27
Number:
  LeetCode 1480
Title:
  Running Sum of 1d Array
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    #iterate nums
    for i in range(1, len(nums)):
      nums[i] += nums[i-1] #running sum

    return nums