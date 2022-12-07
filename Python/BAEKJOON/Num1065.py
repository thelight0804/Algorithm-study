"""
Date:
  22.12.07
Title:
  BAEKJOON 1065번
Project:
  한수
Level:
  Silver 4
Name:
  thelight0804
"""
# standard_input="1"

#input test num
test = int(input())
count = 0

#roop 1 ~ test
for i in range(1, test+1):
  num  = list(map(int, str(i)))
  # ~99 is all arithmetic sequence
  if i < 100:
    count += 1
  # over 100, check arithmetic sequence
  else:
    if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
      count += 1

print(count)