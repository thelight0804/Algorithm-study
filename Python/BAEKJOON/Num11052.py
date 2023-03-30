"""
date: 23.03.29
problem: BAEKJOON 11052
project: 카드 구매하기
level: Silver 1
author: thelight0804
"""
# standard_input = """4
# 1 5 6 7"""
# # 10

#input n, cost
n = int(input())
p = [0] + list(map(int, input().split()))

#memoization
dp = [0 for _ in range(n+1)]

#필요한 카드의 수를 늘려가면서 최대값을 구한다
for i in range(1, n+1):
  for j in range(1, i+1):
    dp[i] = max(dp[i-j] + p[j], dp[i])

print(dp[-1])