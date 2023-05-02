"""
Date:
  23.05.02
Number:
  LeetCode 724
Title:
  Find Pivot Index
Level:
  Easy
Name:
  thelight0804
"""

#### use slice
class Solution(object):
  def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
      if i == 0 and 0 == sum(nums[i+1:]): return i #index 0
      elif i == len(nums) and sum(nums[:i]) == 0: return i #index end
      elif sum(nums[:i]) == sum(nums[i+1:]): return i #found pivot
    
    return -1 #not exists pivot

#### use sum not slice
class Solution(object):
  def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sumArr = sum(nums)
    left = 0
    right = sumArr
    pastPivot = 0

    for i in range(len(nums)):
      left += pastPivot
      right -= nums[i]

      if left == right: return i #found pivot
      pastPivot = nums[i]
      
    return -1 #not exists pivot