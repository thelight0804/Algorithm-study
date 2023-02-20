"""
Date:
  23.02.20
Title:
  BAEKJOON 1874번
Project:
  스택 수열
Level:
  Silver 2
Name:
  thelight0804
"""
# standard_input = """8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1"""
# # + + + + - - + + - + + - - - - -

#input stack length, stack numbers
n = int(input())
a = [int(input()) for i in range(n)]

b = [] #stack list
num = 1 #put stack number
result = [] #result output list

for i in range(n):
  #put number in b
  for j in range(num, a[i]+1):
    b.append(num)
    num += 1
    result.append("+")
  #pop same number
  if b[-1] == a[i]:
    b.pop()
    result.append("-")

#output result
if len(b) == 0:
  print("\n".join(result))
else: #impossible calculation
  print("NO")