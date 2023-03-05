"""
Date:
  23.01.07
Title:
  BAEKJOON 15829번
Project:
  Hashing
Level:
  Bronze 2
Name:
  thelight0804
"""
standard_input = """5
abcde"""
# 1 × 31^0 + 2 × 31^1 + 3 × 31^2 + 4 × 31^3 + 5 × 31^4
# = 1 + 62 + 2883 + 119164 + 4617605
# = 4739715

# input l and string
l = int(input())
a = input()

result = 0

#calculate Hashing
for i in range(l):
  # a = ASCII (a) - 96 = 97 - 96 = 1
  result += (ord(a[i])-96) * (31 ** i)

# mod 1234567891
print(result % 1234567891)