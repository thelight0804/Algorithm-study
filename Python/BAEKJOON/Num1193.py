"""
Date:
  23.01.04
Title:
  BAEKJOON 1193번
Project:
  분수찾기
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input = """4"""

#input num
num = int(input())

#check line, max number of line
#1 / 2,3 / 4,5,6 / 7,8,9,10
line = 0
maxLine = 0
while (num > maxLine):
  line += 1
  maxLine += line

lineGap = maxLine - num

#calculate fraction
#if line is even number
if line % 2 == 0:
  up = line - lineGap
  down = lineGap + 1
else: # if line is odd number
  up = lineGap + 1
  down = line - lineGap
print(f'{up}/{down}')