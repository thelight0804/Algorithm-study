"""
Date:
  23.03.03
Title:
  BAEKJOON 2839번
Project:
  설탕 배달
Level:
  Silver 4
Name:
  thelight0804
"""
# standard_input = """804"""
# # 4



### DP
n = int(input())

l = [0] * (n+1) # memoization

# DP Bottom-Up
for i in range(3, n+1):
  # fixed number
  if i == 3 or i == 5:
    l[i] = 1
  elif i == 4 or i == 7:
    l[i] = -1

  # add 5kg suger
  elif i % 5 == 0:
    l[i] = l[i-5] + 1
  else: # add 3kg suger
    l[i] = l[i-3] + 1

print(l[i])


### Calculation
"""
n = int(input())
bag = 0
while n >= 0:
   #add 5kg
  if n % 5 == 0:
    bag += (n // 5)
    print(bag)
    break
  else: #add 3kg
    n -= 3
    bag += 1
else:
  print(-1)
"""