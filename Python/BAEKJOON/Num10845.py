"""
Date:
  23.02.16
Title:
  BAEKJOON 10845번
Project:
  큐
Level:
  Silver 4
Name:
  thelight0804
"""
# standard_input = """15
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front"""
#1 2 2 0 1 2 -1 0 1 -1 0 3

import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
stack = []

for _ in range(n):
  cmd = input().split()

  if cmd[0] == "push": #push
    stack.append(cmd[1])

  elif cmd[0] == "pop": #pop
    if len(stack) == 0: #empty stack
      output("-1" + "\n")
    else:
      output(str(stack.pop(0)) + "\n")

  elif cmd[0] == "size": #size
    output(str(len(stack)) + "\n")

  elif cmd[0] == "empty": #empty
    if len(stack) == 0:
      output("1" + "\n")
    else:
      output("0" + "\n")

  elif cmd[0] == "front": #front
    if len(stack) == 0: #empty stack
      output("-1" + "\n")
    else:
      output(str(stack[0]) + "\n")

  elif cmd[0] == "back": #back
    if len(stack) == 0: #empty stack
      output("-1" + "\n")
    else:
      output(str(stack[-1]) + "\n")