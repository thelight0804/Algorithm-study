"""
Date:
  22.01.11
Title:
  BAEKJOON 2775번
Project:
  부녀회장이 될테야
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input = """2
# 1
# 3
# 2
# 3"""
# # 35

#input test case
test = int(input())

# roop test case
for i in range(test):
  #input floor and room number
  floor = int(input())
  num = int(input())

  # residents in room
  res = [n for n in range(1, num+1)]

  # up to floor
  for j in range(floor):
    for k in range(1, num):
      # add residents
      res[k] += res[k-1]
    
  #print result
  print(res[-1])