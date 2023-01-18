"""
Date:
  23.01.18
Title:
  BAEKJOON 10989번
Project:
  수 정렬하기 3
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input = """10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7"""

import sys

input = sys.stdin.readline
output = sys.stdout.write

# input test case
test = int(input())

# declaration list
num = [0] * (10000 + 1)

# +1 input number in list index
for i in range(test):
  num[int(input())] += 1

# print number
for i in range(len(num)):
  if(num[i] != 0):
    # print number amount of list
    for j in range(num[i]):
      output(str(i)+'\n')