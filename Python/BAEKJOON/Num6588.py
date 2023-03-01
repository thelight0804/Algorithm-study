"""
Date:
  23.03.01
Title:
  BAEKJOON 6588번
Project:
  골드바흐의 추측
Level:
  Silver 1
Name:
  thelight0804
"""
# standard_input = """8
# 20
# 42
# 0"""
# 8 = 3 + 5
# 20 = 3 + 17
# 42 = 5 + 37

import sys

input = sys.stdin.readline
output = sys.stdout.write

# initialization prime list
prime = [True] * 1000000

# make prime list
for i in range(2, int(len(prime) ** 0.5)+1):
  if prime[i]:
    for j in range(i*2, len(prime), i):
      if prime[j]: prime[j] = False

while True:
  n = int(input())

  # exit
  if n == 0: break
  else:
    for i in range(3, len(prime)):
      #front prime, back prime both true, correct
      if prime[i] and prime[n-i]:
        output(f"{n} = {i} + {n-i}\n")
        break
    # not correct
    else:
      output("Goldbach's conjecture is wrong.")