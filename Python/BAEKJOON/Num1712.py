"""
Date:
  22.12.14
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
num = list(map(int, input().split()))
a = num[0]
b = num[1]
c = num[2]

if(b >= c): #can not BREAK-EVEN POINT
  print(-1)
else: #calculate BREAK-EVEN POINT
  income = c - b
  i = int(a / income)
  print(i+1)