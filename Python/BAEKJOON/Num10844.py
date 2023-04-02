"""
date: 23.04.02
problem: BAEKJOON 10844
project: 쉬운 계단 수
level: Silver 1
author: thelight0804
"""
# standard_input = """3
# """
# #32

#input n
n = int(input())

#memoization
f = [[0] * 10 for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(10):
    #set 1st digit
    if i == 1 and j > 0:
      f[i][j] = 1
    else:
      if j == 0: #~0
        f[i][j] = f[i-1][1]
      elif j == 9: #~9
        f[i][j] = f[i-1][8]
      else: #~1, ~2 ... ~7, ~8
        f[i][j] = f[i-1][j-1] + f[i-1][j+1]

#output result
print(sum(f[n]) % 1000000000)