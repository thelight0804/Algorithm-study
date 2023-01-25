"""
Date:
  23.01.25
Title:
  BAEKJOON 11653번
Project:
  소인수분해
Level:
  Bronze 1
Name:
  thelight0804
"""
standard_input = """9991"""
# 2 2 2 3 3

n = int(input())
i = 2

# nothing output if n is 1
while(n != 1):
  # Factoryization is possible
  if(n % i == 0):
    print(i)
    n /= i
  # Factoryization is not possible
  else:
    i += 1
