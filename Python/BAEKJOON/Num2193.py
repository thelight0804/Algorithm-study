"""
date: 23.03.10
problem: BAEKJOON 2193
project: 이친수
level: Silver 3
author: thelight0804
"""
# standard_input = """3"""
# # 2

#input n
n = int(input())
f = [0] * (n+1) #memoization

for i in range(1, n+1):
  if i == 1: f[1] = 1
  elif i == 2: f[2] = 1
  else: #Dynamic Programming
    f[i] = f[i-1] + f[i-2]

#output result
print(f[-1])