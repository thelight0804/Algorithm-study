"""
Date:
  23.03.07
Title:
  BAEKJOON 9095번
Project:
  1, 2, 3 더하기
Level:
  Silver 3
Name:
  thelight0804
"""
standard_input = """3
4
7
10"""
# 7 44 274

#input testcase
t = int(input())

for _ in range(t):
  #input number
  n = int(input())
  #memoization
  f = [0] * (n + 1)
  
  for i in range(1, n + 1):
    # stuck number
    if i == 1: f[i] = 1
    elif i == 2: f[i] = 2
    elif i == 3: f[i] = 4
    # Dynamic Programming
    else: f[i] = f[i-1] + f[i-2] + f[i-3]

  #output result
  print(f[-1])