"""
Date:
  23.03.02
Title:
  BAEKJOON 10773번
Project:
  제로
Level:
  Silver 4
Name:
  thelight0804
"""
# standard_input = """10
# 1
# 3
# 5
# 4
# 0
# 0
# 7
# 0
# 0
# 6"""
# # 7

# input k
k = int(input())
s = [] # stack

for i in range(k):
  n = int(input())
  if n == 0: s.pop()
  else: s.append(n)

# output sum
print(sum(s))