"""
Date:
  23.02.21
Title:
  BAEKJOON 1406번
Project:
  에디터
Level:
  Silver 2
Name:
  thelight0804
"""
# standard_input = """dmih
# 11
# B
# B
# P x
# L
# B
# B
# B
# P y
# D
# D
# P z"""

import sys
input = sys.stdin.readline
output = sys.stdout.write

a = list(input().strip()) #stack 1
b = [] #stack 2

m  = int(input()) #command count

for _ in range(m):
  cmd = input().split() #input command

  if cmd[0] == 'L':
    # move curser left
    if len(a) != 0:
      b.append(a.pop())
  
  if cmd[0] == 'D':
    # move curser right
    if len(b) != 0:
      a.append(b.pop())
  
  if cmd[0] == 'B':
    # delete character
    if len(a) != 0:
      a.pop()
  
  if cmd[0] == 'P':
    # add character
    a.append(cmd[1])

# reverse b to put A
b.reverse()

output(''.join(a+b))