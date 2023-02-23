"""
Date:
  23.02.23
Title:
  BAEKJOON 1934번
Project:
  최소공배수
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input = """3
# 1 45000
# 6 10
# 13 17"""
# # 45000 30 221

#input test case
n = int(input())

for _ in range(n):
  #input a, b
  a, b = map(int, input().split())

  #calculate GCD
  c, d = a, b
  while c != 0:
    d %= c
    c, d = d, c
  gcd = d

  #calculate LCM
  print(int(a * b / gcd))


### use math.lcm
"""
import math

#input test case
n = int(input())

for _ in range(n):
  #input a, b
  a, b = map(int, input().split())
  print(math.lcm(a, b))
"""