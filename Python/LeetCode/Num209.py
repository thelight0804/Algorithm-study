"""
Date:
  23.05.03
Number:
  LeetCode 209
Title:
  Find Pivot Index
Level:
  Easy
Name:
  thelight0804
"""
class Solution(object):
  def minSubArrayLen(self, target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    if sum(nums) < target: return 0 #no such target

    left = right = total = 0
    count = len(nums) + 1 #set max count

    for right in range(len(nums)):
      total += nums[right] #add right numbers
      while total >= target:
        count = min(count, right - left + 1)
        total -= nums[left] #sub left number
        left += 1 #move left
    
    return count