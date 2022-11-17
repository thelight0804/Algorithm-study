"""
Date:
  22.11.13
Title:
  BAEKJOON 2577번
Project:
  숫자의 개수
Level:
  Bronze 2
Name:
  thelight0804
"""
# standard_input="""150
# 266
# 427
# """

from functools import reduce

#input three number
a = [int(input()) for i in range (3)]
count = [0 for i in range(10)] # number count list

#multiply list a
mult = str(reduce(lambda x, y: x* y, a))

for i in range(10):
  print(mult.count(str(i)))