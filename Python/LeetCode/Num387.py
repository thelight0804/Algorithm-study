"""
Date:
  23.05.10
Number:
  LeetCode 387
Title:
  First Unique Character in a String
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    hashTable = {}

    #add hashTable
    for i in range(len(s)):
      if s[i] in hashTable:
        hashTable[s[i]] += 1 #add count
      else:
        hashTable[s[i]] = 1

    #search first non-repeating charater
    for i in range(len(s)):
      if hashTable[s[i]] == 1:
        return i

    return -1 # not exist non-repeating charater