"""
Date:
  23.05.14
Number:
  LeetCode 347
Title:
  Top K Frequent Elements
Level:
  Medium
Name:
  thelight0804
"""

class Solution(object):
  def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    table = {}
    result = []
    
    #add items
    for key in nums:
      if key not in table: table[key] = 1
      else: table[key] += 1
    
    #sort table
    sortTable = sorted(table.items(), key = lambda x: -x[1])
    print(sortTable)

    #add result
    for i in range(k):
      result.append(sortTable[i][0])
    
    return result