"""
Date:
  23.02.17
Title:
  BAEKJOON 10866번
Project:
  덱
Level:
  Silver 4
Name:
  thelight0804
"""
# standard_input = """15
# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front"""

import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

#input command test case
n = int(input())

#make a new deque
d = deque()

for _ in range(n):
  #input command
  cmd = input().split()
  
  if cmd[0] == "push_front":
    d.appendleft(cmd[1])

  elif cmd[0] == "push_back":
    d.append(cmd[1])

  elif cmd[0] == "pop_front":
    if(len(d) == 0):  output("-1" + "\n") #empty deque
    else: output(d.popleft() + "\n")

  elif cmd[0] == "pop_back":
    if(len(d) == 0):  output("-1" + "\n") #empty deque
    else: output(d.pop() + "\n")

  elif cmd[0] == "size":
    output(str(len(d)) + "\n")

  elif cmd[0] == "empty":
    if(len(d) == 0):  output("1" + "\n") #empty deque
    else: output("0" + "\n")

  elif cmd[0] == "front":
    if(len(d) == 0):  output("-1" + "\n") #empty deque
    else: output(str(d[0]) + "\n")

  elif cmd[0] == "back":
    if(len(d) == 0):  output("-1" + "\n") #empty deque
    else: output(str(d[-1]) + "\n")