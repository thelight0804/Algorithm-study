"""
date: 23.03.30
problem: BAEKJOON 16194
project: 카드 구매하기 2
level: Silver 1
author: thelight0804
"""
# standard_input = """4
# 5 2 8 10
# """
# #4

#input cards
n = int(input())
p = [0] + list(map(int, input().split()))

#memoization
#dp list 없이 p로만도 구현 가능
dp = [0] + [max(p) for _ in range(n)]

#Dynamic Algorism
for i in range(1, n+1):
  for j in range(i):
    #set min cost
    dp[i] = min(dp[j] + p[i-j], dp[i])

#output result
print(dp[-1])