"""
Date:
  23.03.06
Number:
  LeetCode 322
Title:
  Coin Change
Level:
  Medium
Name:
  thelight0804
"""

class Solution(object):
  def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    coins.sort()

    f = [10001] * (amount + 1)
    f[0] = 0 # 0 coin is always 0
    
    # set 1 coin
    for i in range(len(coins)):
      if coins[i] <= amount:
        f[coins[i]] = 1
    
    for i in range(1, len(f)):
      for j in coins: # compare coins
        if i - j >= 0 and f[i - j] + 1 < f[i]:
          # change coin count
          f[i] = f[i - j] + 1

    # output result
    if f[-1] == 10001: return -1
    else: return f[-1]