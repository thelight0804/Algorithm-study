"""
Date:
    22.11.08
Title:
    BAEKJOON 2869번
Project:
    달팽이는 올라가고 싶다
Level:
    Silver 5
Name:
    thelight0804
"""
standard_input = '5 1 6'

import sys
input = sys.stdin.readline().rstrip

#input num
a, b, v = map(int, input().split(" "))

#sub height from down
v -= b

#climb height of one day
climb = a - b

day = int(v / climb)

#remain height
if (v % climb) != 0:
  day += 1

#print result
print(day)