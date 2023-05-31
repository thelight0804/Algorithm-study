"""
Date:
  23.05.31
Number:
  LeetCode 1342
Title:
  Number of Steps to Reduce a Number to Zero
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def numberOfSteps(self, num):
    """
    :type num: int
    :rtype: int
    """
    steps = 0

    while num != 0:
      if num % 2 == 0: #even
        num /= 2
      else: #odd
        num -= 1
      steps += 1 #add count
    
    return steps