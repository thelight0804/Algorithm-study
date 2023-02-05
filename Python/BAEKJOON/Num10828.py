"""
Date:
  23.02.05
Title:
  BAEKJOON 10828번
Project:
  스택
Level:
  Silver 4
Name:
  thelight0804
"""
# standard_input = """7
# pop
# top
# push 123
# top
# pop
# top
# pop"""

import sys

input = sys.stdin.readline
output = sys.stdout.write

#input test number
test = int(input())

stack = [] #stack list

for i in range(test):
  #input command
  cmd = input().split()

  if(cmd[0] == "push"): #push
    stack.append(cmd[1])
  elif(cmd[0] == "pop"): #pop
    if(len(stack) != 0):
      output(str(stack[-1])+'\n')
      stack.pop()
    else: # empty stack
      output(str(-1)+'\n')
  elif(cmd[0] == "size"): #size
    output(str(len(stack))+'\n')
  elif(cmd[0] == "empty"): #empty
    if(len(stack) == 0): # empty stack
      output(str(1)+'\n')
    else:
      output(str(0)+'\n')
  elif(cmd[0] == "top"): #top
    if(len(stack) != 0):
      output(str(stack[-1])+'\n')
    else: # empty stack
      output(str(-1)+'\n')