"""
Date:
  23.05.14
Number:
  LeetCode 692
Title:
  Top K Frequent Words
Level:
  Medium
Name:
  thelight0804
"""

class Solution(object):
  def topKFrequent(self, words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    table = {}
    answer = []

    #add words
    for s in words:
      if table.get(s) is None:
        table[s] = 1
      else:
        table[s] += 1
    
    #sort table
    arr = sorted(table.items(), key=lambda x: (-x[1], x[0]))

    #add answer words
    for i in range(k):
      answer.append(arr[i][0])
    
    return answer