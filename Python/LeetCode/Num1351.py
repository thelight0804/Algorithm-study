"""
Date:
  23.06.08
Number:
  LeetCode 1351
Title:
  Count Negative Numbers in a Sorted Matrix
Level:
  Easy
Author:
  thelight0804
"""

class Solution(object):
  def countNegatives(self, grid):
    #gird col length
    n = len(grid[0])
    cnt = 0 #count

    #iterate grid
    for row in grid:
      l, r = 0, n - 1 #set left, right
      while l <= r: #binary search
        mid = (l + r) // 2 #set mid index
        if row[mid] < 0: #move right index
          r = mid - 1
        else: #move left index
          l = mid + 1
      #add negative elements
      cnt += n - l
    
    return cnt