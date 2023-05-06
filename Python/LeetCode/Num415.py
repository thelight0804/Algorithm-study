"""
Date:
  23.05.05
Number:
  LeetCode 415
Title:
  Add Strings
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def addStrings(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    #two pointer
    p1 = len(num1) - 1
    p2 = len(num2) - 1

    carry = 0
    result = []

    while max(p1, p2) >= 0:
      #char to int
      n1 = int(num1[p1])
      n2 = int(num2[p2])

      if p1 < 0: #end of number list
        n1 = 0
      else: #next char number
        p1 -= 1 
      if p2 < 0:
        n2 = 0
      else:
        p2 -= 1

      #add two numbers
      digitSum = carry + n1 + n2
      carry = digitSum / 10
      mod = digitSum % 10
      result.append(str(mod))
    
    if carry != 0:
      result.append(str(carry))

    #output answer
    result.reverse()    
    return ''.join(result)