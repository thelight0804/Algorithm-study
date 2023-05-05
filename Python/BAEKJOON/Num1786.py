"""
Date:
  23.05.05
Problem:
  BAEKJOON 1786번
Project:
  찾기
Level:
  Platinum 5
Author:
  thelight0804
"""

# standard_input = """ABC ABCDAB ABCDABCDABDE
# ABCDABD"""
# # 1
# # 16

# standard_input = """onionionskys
# onions"""
# # 1
# # 4

# standard_input = """abacabacabacababacabacabacabab
# abacabacabacabab"""
# # 2
# # 1 15

# standard_input = """abacabacabacababacabacabacabab
# aabcaab"""
# # 2
# # 1 15

t = input()
p = input()
tLen = len(t)
pLen = len(p)

#set LPS
lps = [0] * pLen
prev = 0
i = 1

while i < pLen:
  if p[i] == p[prev]: #add lps count
    prev += 1
    lps[i] = prev
    i += 1
  elif prev == 0: #set lps 0
    lps[i] = 0
    i += 1
  else: #set prev
    prev = lps[prev - 1]

#search
count = 0
index = []
p1 = p2 = 0 #set two pointer
while p1 < tLen:
  # print(p1, p2, t[p1], t[p2])
  if t[p1] == p[p2]: #match character
    p1 += 1
    p2 += 1
    if p2 == pLen: #match string
      count += 1
      index.append(p1 - pLen + 1)
      p2 = lps[p2-1] #reset p2
  # not match character
  elif p2 == 0:
    p1 += 1
  else:
    p2 = lps[p2-1] #set p2

#output result
print(count)
for i in index:
  print(i, end=' ')