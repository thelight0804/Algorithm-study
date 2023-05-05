"""
Date:
  23.05.05
Number:
  LeetCode 28
Title:
  Find the Index of the First Occurrence in a String
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    n = len(haystack)
    m = len(needle)

    # except
    if m > n: return -1

    # set lps
    lps = [0] * m
    prev = 0 #move left index
    i = 1 #move right index
    while i < m:
      if needle[prev] == needle[i]: #add lps count
        prev += 1
        lps[i] = prev
        i += 1
      elif prev == 0: #not match needle[0]
        lps[i] = 0
        i += 1
      else: #set previous lps
        prev = lps[prev - 1]
    
    #searching
    p1 = p2 = 0
    while p1 < n:
      if haystack[p1] == needle[p2]: #match character
        p1 += 1
        p2 += 1
        if p2 == m: #find match string
          return p1 - m
      elif p2 == 0: #not match needle[0]
        p1 += 1
      else: p2 = lps[p2 - 1] #set previous lps

    return -1 #not exist needle in haystack