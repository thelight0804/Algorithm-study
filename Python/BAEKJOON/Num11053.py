"""
date: 23.03.24
problem: BAEKJOON 11053
project: 가장 긴 증가하는 부분 수열
level: Silver 2
author: thelight0804
"""
# standard_input = """6
# 10 20 10 30 20 50"""
# # 4

#input a
a = int(input())
l = list(map(int, input().split()))

#memorization
f = [0 for i in range(a)]

#Dynamic Algorithm
for i in range(a):
  #fix number
  if i == 0: f[0] = 1
  else:
    #search small number of f[j]
    for j in range(i, -1, -1):
      #find long count
      if l[j] < l[i] and f[j] > f[i]:
        f[i] = f[j]
    f[i] += 1 #set count

#print result
print(max(f))