"""
Date:
  23.05.30
Number:
  LeetCode 412
Title:
  Fizz Buzz
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = [str(i+1) for i in range(n)]

    #divisible by 3
    for i in range(2, n, 3):
      result[i] = "Fizz"
    
    #divisible by 5
    for i in range(4, n, 5):
      result[i] = "Buzz"
    
    #divisible by 3 and 5
    for i in range(14, n, 15):
      result[i] = "FizzBuzz"
    
    return result