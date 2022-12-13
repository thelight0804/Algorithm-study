"""
Date:
  22.12.13
Title:
  BAEKJOON 2750번
Project:
  수 정렬하기
Level:
  Bronze 2
Name:
  thelight0804
"""
# standard_input="""5
# 5
# 2
# 3
# 4
# 1
# """
# input test case and number
test = int(input())
num = [int(input()) for i in range (test)]

num.sort()

# print num List
for i in range(test):
  print(num[i])