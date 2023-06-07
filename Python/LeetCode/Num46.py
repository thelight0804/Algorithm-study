"""
Date:
  23.06.07
Number:
  LeetCode 46
Title:
  Permutations
Level:
  Medium
Author:
  thelight0804
"""

class Solution(object):
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    output = [] #result

    def bt(perm):
      #return condition
      if len(perm) == len(nums):
        output.append(copy.deepcopy(perm)) #deep copy
        return

      #backtracking process
      for num in nums:
        if num not in perm:
          #call recursion
          perm.append(num)
          bt(perm)
          perm.pop()
    
    #start backtracking
    bt([])

    return output