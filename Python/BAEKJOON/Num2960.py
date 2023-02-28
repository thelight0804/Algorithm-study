"""
Date:
  23.02.28
Title:
  BAEKJOON 2960번
Project:
  에라토스테네스의 체
Level:
  Silver 4
Name:
  thelight0804
"""
# standard_input = """7 3"""
# #9

n, k = map(int, input().split())
cnt = 0

### use True, False
si = [True] * (n + 1)

for i in range(2, len(si)):
  # check multiple
  for j in range(i, len(si), i):
    if si[j] :
      cnt += 1
      if cnt == k: # output result
        print(j)
        break
      si[j] = False # multiple


### use number list
"""
# 2 ~ n list
si = [i for i in range(2, n+1)]

for i in range(len(si)):
  if si[i] != 0: # si[i] 0 is skip
    num = si[i] # fixed multiple

    # find multiple to num
    for j in range(i, len(si)):
      if si[j] == 0: continue
      elif si[j] % num == 0:
        cnt += 1
        #output result
        if cnt == k:
          print(si[j])
          break
        #change to 0, multiples
        si[j] = 0
"""