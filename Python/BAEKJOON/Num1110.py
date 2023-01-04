"""
Date:
  22.01.02
Title:
  BAEKJOON 1110번
Project:
  더하기 사이클
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input = '71'

#input number
num = int(input())
d = num

cnt = 0 #count

while(True):
  cnt += 1 #increase count 

  # a + b = c
  a = d//10
  b = d % 10
  c = (a + b) % 10

  # new number
  d = (b * 10) + c

  #print result count
  if(num == d):
    print(cnt)
    break