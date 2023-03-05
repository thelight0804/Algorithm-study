"""
Date:
  22.11.09
Title:
  BAEKJOON 2439번
Project:
  별 찍기 - 2
Level:
  Bronze 4
Name:
  thelight0804
"""

standard_input = '5'

#input num
num = int(input())

#print stars
for i in range(num-1, -1, -1):
  for j in range(i):
    print(" ", end = '')
  for k in range(num-i):
    print("*", end = '')
  print('')

# #print stars
# for i in range(1, num + 1):
#   print(" " * (num - i) + "*" * i)