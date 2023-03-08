"""
Date:
  23.03.08
Title:
  BAEKJOON 2579번
Project:
  계단 오르기
Level:
  Silver 3
Name:
  thelight0804
"""
# standard_input = """6
# 10
# 20
# 15
# 25
# 10
# 20"""
# # 75

s = int(input())
n = [int(input()) for _ in range(s)]
dp = n.copy() # dp list

for i in range(s):
  # stuck number
  if i == 0: continue
  elif i == 1: dp[1] += dp[0]
  elif i == 2:
    dp[2] += max(n[0], n[1])
  # Dynamic Algorithm
  else:
    dp[i] += max(dp[i-2], n[i-1] + dp[i-3])

# output result
print(dp[-1])