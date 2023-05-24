"""
Date:
  23.05.24
Number:
  LeetCode 78
Title:
  Subsets
Level:
  Medium
Name:
  thelight0804
"""

class Solution(object):
  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    subset = [] #sotre subsets

    def bt(idx):
      #exit recursive method
      if idx == len(nums):
        result.append(subset[:]) #deep copy
        return

      num = nums[idx] #get number

      #BackTracking of include number
      subset.append(num)
      bt(idx+1)

      #BackTracking of exclude number
      subset.pop()
      bt(idx+1)

    bt(0) #start BackTracking

    return result