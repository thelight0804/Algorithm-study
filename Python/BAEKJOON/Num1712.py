"""
Date:
  22.01.02
Title:
  BAEKJOON 1712번
Project:
  손익분기점
Level:
  Bronze 2
Name:
  thelight0804
"""
# standard_input = '3 2 1'

#input a, b, c
a, b, c = map(int, input().split())

if(b >= c): #can not BREAK-EVEN POINT
  print(-1)
else: #calculate BREAK-EVEN POINT
  income = c - b
  print(int(a / income)+1)