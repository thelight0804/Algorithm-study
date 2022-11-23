"""
Date:
  22.11.22
Title:
  BAEKJOON 1085번
Project:
  직사각형에서 탈출
Level:
  Bronze 3
Name:
  thelight0804
"""
# standard_input='1 1 5 5'

#input String
x, y, w, h = map(int, input().split())

print(min(x, y, w - x, h - y))