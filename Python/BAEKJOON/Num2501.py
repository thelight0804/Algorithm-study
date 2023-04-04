"""
Date:
  23.04.04
Problem:
  BAEKJOON 2501번
Project:
  약수 구하기
Level:
  Bronze 3
Author:
  thelight0804
"""

# standard_input = """6 3"""
# #3

#input n, k
n, k = map(int, input().split())
div = []

for i in range(1, n+1):
  #check divisor
  if n % i == 0:
    div.append(i)

#output result
if len(div) < k: #no k divisor
  print(0)
else:
  print(div[k-1])