"""
Date:
  23.02.03
Title:
  BAEKJOON 7568번
Project:
  덩치
Level:
  Silver 5
Name:
  thelight0804
"""
# standard_input = """5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155"""
# # 2 2 1 2 5

#input people height, weight
test = int(input())
size = []

for i in range(test):
  h, w = map(int, input().split())
  size.append((h, w))

for i in size:
  rank = 1
  #compare different people height, weight
  for j in size:
    if(i[0] < j[0] and i[1] < j[1]):
      rank += 1
  #output rank
  print(rank, end=" ")