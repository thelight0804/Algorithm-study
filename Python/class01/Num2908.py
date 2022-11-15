"""
Date:
  22.11.15
Title:
  BAEKJOON 2908번
Project:
  상수
Level:
  Bronze 2
Name:
  thelight0804
"""
# standard_input = """839 237"""

#input num
a, b = map(int, input().split(' '))

#reverse a and b
revA = 0
revB = 0

temp = 0

#number extraction
#figures up
#add number extraction
#figures down
for i in range(3):
  temp = a % 10
  revA *= 10
  revA += temp
  a = int(a / 10)

for i in range(3):
  temp = b % 10
  revB *= 10
  revB += temp
  b = int(b / 10)

print(max(revA, revB))

"""
#input num
a, b = input().split(' ')

a = int(a[::-1])
b = int(b[::-1])

print(max(a, b))
"""