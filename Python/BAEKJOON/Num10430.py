"""
Date:
  23.02.22
Title:
  BAEKJOON 10430번
Project:
  나머지
Level:
  Bronze 5
Name:
  thelight0804
"""
# standard_input = """5 8 4"""
# #1 (A+B)%C
# #1 ((A%C) + (B%C))%C
# #0 (A×B)%C
# #0 ((A%C) × (B%C))%C

a, b, c = map(int, input().split())

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)
