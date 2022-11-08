"""
Date:
    22.10.28
Title:
    BAEKJOON 10807번
Project:
    개수 세기
Level:
    Bronze 5
Name:
    thelight0804
"""

# standard_input = '''11
# 1 4 1 2 4 2 4 2 3 4 4
# 2
# '''

#input
test = int(input())
list = list(map(int, input().split(' ')))
n = int(input())
count = 0

#find n index
for i in range(test):
  if list[i] == n:
    count += 1
print(count)