"""
Date:
    22.10.27
Title:
    BAEKJOON 15552번
Project:
    빠른 A+B
Level:
    Bronze 5
Name:
    thelight0804
"""
# standard_input = '500 5'
import sys

test = int(sys.stdin.readline().rstrip())

for i in range(test):
  a, b = map(int, sys.stdin.readline().rstrip().split(" "))
  print(a + b)