"""
Date:
  23.05.10
Number:
  LeetCode 1
Title:
  Two Sum
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def twoSum(self, nums, target):
    hashTable = {} #create hash table

    for idx, num in enumerate(nums):
      #search match number
      matchNum = target - num
      if matchNum in hashTable:
        return [idx, hashTable.get(matchNum)]

      #insert number element
      hashTable[num] = idx