"""
Date:
  23.06.05
Number:
  LeetCode 1502
Title:
  Can Make Arithmetic Progression From Sequence
Level:
  Easy
Author:
  thelight0804
"""

class Solution(object):
  def canMakeArithmeticProgression(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    maxValue = max(arr)
    minValue = min(arr)

    # arithmetic progression is always true if diff is 0
    if maxValue - minValue == 0:
      return True
    
    # not arithmetic progression
    if (maxValue - minValue) % (len(arr) - 1) != 0:
      return False
    
    #difference two element
    diff = (maxValue - minValue) // (len(arr) - 1)
    
    #initialize set to prevent same element
    numSet = set()

    #check arithmetic progression
    for val in arr:
      if (val - minValue) % diff != 0:
        return False
      else: numSet.add(val)
    
    #return result
    return len(numSet) == len(arr)