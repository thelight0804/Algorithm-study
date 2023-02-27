"""
Date:
  23.02.24
Title:
  BAEKJOON 1676번
Project:
  최소공배수
Level:
  Silver 1
Name:
  thelight0804
"""
# standard_input = """25"""
# # 2



###for
n = int(input())
p = 1 #factoritail

#calculation factorial
for i in range(1, n+1):
  p *= i
sP = str(p)

#counting '0'
cnt = 0
for j in range(len(sP)-1, 0, -1):
  if sP[j] == '0': cnt += 1
  else: break

#output result
print(cnt)


"""
###math.factorial
import math

n = int(input())

#calculation factorial
sP = str(math.factorial(n))

#counting '0'
cnt = 0
for j in range(len(sP)-1, 0, -1):
  if sP[j] == '0': cnt += 1
  else: break

print(cnt)
"""