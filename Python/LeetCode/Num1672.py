"""
Date:
  23.05.29
Number:
  LeetCode 1672
Title:
  Richest Customer Wealth
Level:
  Easy
Name:
  thelight0804
"""

class Solution(object):
  def maximumWealth(self, accounts):
    wealth = 0 #max money

    for account in accounts:
      #check wealth
      wealth = max(sum(account), wealth)
    
    return wealth