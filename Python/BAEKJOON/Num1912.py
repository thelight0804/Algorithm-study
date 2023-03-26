"""
date: 23.03.26
problem: BAEKJOON 1912
project: 연속합
level: Silver 2
author: thelight0804
"""
# standard_input = """5
# -1 -2 -3 -4 -5"""
# # 33

#input
n = int(input())
f = list(map(int, input().split()))

#Dynamic Algorism
for i in range(1, n):
  f[i] = max(f[i-1] + f[i], f[i])

#output
print(max(f))