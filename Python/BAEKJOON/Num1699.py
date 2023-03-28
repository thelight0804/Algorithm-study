"""
date: 23.03.28
problem: BAEKJOON 1699
project: 제곱수의 합
level: Silver 2
author: thelight0804
"""
# standard_input = """11"""
# # 3

#input n
n = int(input())

#memoization default 1^1 count
f = [i for i in range(n+1)]

#Dynamic Algorism 
for i in range(1, n+1):
  for j in range(1, i):
    #check square number
    if j*j > i:
      break
    elif f[i-(j*j)] + 1 < f[i]:
      f[i] = f[i-(j*j)] + 1

#output result
print(f[-1])