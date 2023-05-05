"""
Date:
  23.05.05
Number:
  LeetCode 125
Title:
  Valid Palindrome
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """

    s = s.lower() #change lower case
    l = 0 #left
    r = len(s) - 1 #right

    while l < r:
      #check alphabet or number
      if not s[l].isalnum():
        l += 1
        continue
      if not s[r].isalnum():
        r -= 1
        continue
      #check match character
      if s[l] == s[r]:
        l += 1
        r -= 1
      else: #not match
        return False
  
    return True