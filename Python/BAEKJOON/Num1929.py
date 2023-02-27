"""
Date:
  23.02.27
Title:
  BAEKJOON 1929번
Project:
  소수 구하기
Level:
  Silver 3
Name:
  thelight0804
"""
# standard_input = """3 16"""
# #3, 5, 7, 11, 13

import sys, math

input = sys.stdin.readline
output = sys.stdout.write

# input m, n
m, n = map(int, input().split())

for i in range(m, n+1):
  # 1 is not prime
  if i == 1: continue

  # check prime
  for j in range(2, int(i**0.5)+1):
    if i % j == 0: break
  # without break to out for
  else: print(i)