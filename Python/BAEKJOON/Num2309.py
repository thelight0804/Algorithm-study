"""
Date:
  23.01.25
Title:
  BAEKJOON 2309번
Project:
  일곱 난쟁이
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input = """20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13"""
# # 7 8 10 13 19 20 23

from itertools import combinations

#input children dwarf
n = [int(input()) for i in range(9)]

#sort n
n.sort()

gap = sum(n) - 100

# roop 2 Combination
for i in combinations(n, 2):
  # fake dwarf
  if(sum(i) == gap):
    # remove list value
    n.remove(i[0])
    n.remove(i[1])
    break

# output result
for i in range(7):
  print(n[i])

########################################

#input children dwarf
n = [int(input()) for i in range(9)]

#sort n
n.sort()

gap = sum(n) - 100

# search gap from list
for i in range(8, 0, -1):
  for j in range(1, i+1):
    # descending search
    temp = n[i] + n[i-j]
    if(temp < gap):
      break
    # fake dwarf
    if(temp == gap):
      del n[i], n[i-j]
      break
  if(len(n) == 7):
     break

for i in range(7):
  print(n[i])