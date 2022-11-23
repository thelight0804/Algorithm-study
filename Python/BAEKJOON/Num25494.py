"""
Date:
  22.11.23
Title:
  BAEKJOON 25494번
Project:
  단순한 문제 (Small)
Level:
  Bronze 4
Name:
  thelight0804
"""
# standard_input="""2
# 1 2 3
# 3 2 4
# """
test = int(input())
for i in range(test):
  a, b, c = map(int, input().split())
  print(min(a, b, c))