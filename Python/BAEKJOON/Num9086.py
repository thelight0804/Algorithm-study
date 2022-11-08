"""
Date:
    22.11.03
Title:
    BAEKJOON 9086번
Project:
    문자열
Level:
    Bronze 5
Name:
    thelight0804
"""
# standard_input = 'AB'

test = int(input())

for i in range(test):
  str = input()

  print(str[0], end="")
  print(str[-1])