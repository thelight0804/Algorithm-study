"""
Date:
  23.03.05
Number:
  LeetCode 64
Title:
  Minimum Path Sum
Level:
  Medium
Name:
  thelight0804
"""

class Solution(object):
  def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # grid[y][x]
    for y in range(len(grid)):
      for x in range(len(grid[y])):
        # grid[0][0]
        if y == 0 and x == 0: continue

        elif y == 0: # grid[0][x]
          grid[y][x] += grid[y][x-1]
        elif x == 0: # grid[y][0]
          grid[y][x] += grid[y-1][x]

        # add min cost
        else:
          grid[y][x] += min(grid[y-1][x], grid[y][x-1])
    return grid[-1][-1]