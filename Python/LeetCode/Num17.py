"""
Date:
  23.04.05
Number:
  LeetCode 17
Title:
  Letter Combinations of a Phone Number
Level:
  Medium
Author:
  thelight0804
"""

class Solution(object):
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    result = []

    # set char to phone number
    hashMap = {
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz'
    }

    """
    index: str
      digits index
    letter: str
      phone char
    """
    def bt(index, letter):
      # exit function
      if len(letter) == len(digits):
        result.append(letter)
        return

      for i in range(index, len(digits)):
        num = digits[i]  # phone number
        chars = hashMap[num]  # chars list
        for j in chars:  # loop char
          bt(i+1, letter+j)  # Recursive Function

    # empty input
    if len(digits) == 0:
      return result

    # start Backtracking
    bt(0, '')

    # output result
    return result
