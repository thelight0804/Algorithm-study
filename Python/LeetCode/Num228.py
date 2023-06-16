"""
Date:
  23.06.16
Number:
  LeetCode 228
Title:
   Summary Ranges
Level:
  Easy
Author:
  thelight0804
"""

class Solution(object):
  def summaryRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if not nums: return []

    result = [] #output result

    ran = [] #[n1, n2]

    for num in nums:
      ran.append(num) #add first number
      if ran[-1] - ran[0] >= len(ran): #not sort +1
        ranges = str(ran[0])
        if len(ran) > 2: #add ranges
          ranges += "->" + str(ran[-2])
        result.append(ranges) #append result
        ran = [ran[-1]] #set next number
      
    #append last range to result
    ranges = str(ran[0])
    if len(ran) > 1:
      ranges += "->" + str(ran[-1])
    result.append(ranges)
    
    return result