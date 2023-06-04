"""
Date:
  23.06.04
Number:
  LeetCode 383
Title:
  Ransom Note
Level:
  Easy
Author:
  thelight0804
"""

class Solution(object):
  def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    
    #create counter objects
    note = Counter(ransomNote)
    mag = Counter(magazine)

    print(note)

    #check counter objects
    if note & mag == note: return True
    else: return False