"""
Date:
  23.03.07
Title:
  BAEKJOON 11726번
Project:
  2×n 타일링
Level:
  Silver 3
Name:
  thelight0804
"""
# standard_input = """9"""
# # 55

n = int(input())
f = [0] * (n+1) #memoization

f[1] = 1
if n == 1:
  print(f[1])

else:
  for i in range(2, n+1):
    f[2] = 2 #stuck number
    if i > 2: #Dynamic Programming
      f[i] = f[i-1] + f[i-2]

  #output
  print(f[-1] % 10007)


### use list.append
"""
n = int(input())
f = [0,1,2] #memoization

#Dynamic Programing
for i in range(3, n+1):
  f.append(f[i-1] + f[i-2])

#output result
print(f[n] % 10007)
"""