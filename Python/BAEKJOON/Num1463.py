"""
Date:
  23.03.04
Title:
  BAEKJOON 1463번
Project:
  1로 만들기
Level:
  Silver 3
Name:
  thelight0804
"""
# standard_input = """10"""
# # 3

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
f = [0] * (n+1) #memoization

for i in range(2, n+1):
  if i == 2 or i == 3: #stuck value
    f[i] = 1
  else:
    # check all min f[i-1], f[i//2], f[i//3]
    f[i] = f[i-1] + 1
    if i % 2 == 0:
      f[i] = min(f[i], f[i//2] + 1)
    if i % 3 == 0:
      f[i] = min(f[i], f[i//3] + 1)

#output result
output(str(f[-1]))