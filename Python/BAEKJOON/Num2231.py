"""
Date:
  22.11.23
Title:
  BAEKJOON 2231번
Project:
  분해합
Level:
  Bronze 2
Name:
  thelight0804
"""
# standard_input='1'

#input num
num = int(input())
result = 0

for i in range(1, num+1):
  # a = digits num
  a = list(map(int, str(i)))
  result = i + sum(a)
  if result == num:
    print(i)
    break
  # do not have generator
  if i == num:
    print(0)
    break