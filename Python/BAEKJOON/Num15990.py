"""
date: 23.03.10
problem: BAEKJOON 15990
project: 1, 2, 3 더하기 5
level: Silver 2
author: thelight0804
"""
# standard_input = """3
# 4
# 7
# 10"""
# # 3, 9, 27

#dp reset
f = [[0 for i in range(4)] for i in range(100001)]

#set dp
for i in range(100001):
  #stuck number
  #count of [0, ~+1, ~+2, ~+3]
  if i == 1:
    f[1] = [0, 1, 0, 0]
  elif i == 2:
    f[2] = [0, 0, 1, 0]
  elif i == 3:
    f[3] = [0, 1, 1, 1]
  #Dynamic Programming
  else:
    f[i][1] = (f[i-1][2] + f[i-1][3]) % 1000000009
    f[i][2] = (f[i-2][1] + f[i-2][3]) % 1000000009
    f[i][3] = (f[i-3][1] + f[i-3][2]) % 1000000009

#input testcase
t = int(input())

for _ in range(t):
  n = int(input()) #input n
  print(sum(f[n]) % 1000000009)