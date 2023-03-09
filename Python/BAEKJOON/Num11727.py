"""
Date:
  23.03.09
Title:
  BAEKJOON 11727번
Project:
  2×n 타일링 2
Level:
  Silver 3
Name:
  thelight0804
"""
# standard_input = """12"""
# # 2731

n = int(input())
f = [0] * (n+1) #memoization

for i in range(1, n+1):
  #stuck number
  if i == 1: f[1] = 1
  elif i == 2: f[2] = 3
  #Dynamic Programming
  else: f[i] = f[i-1] + (f[i-2] * 2)

#output result
print(f[-1] % 10007)