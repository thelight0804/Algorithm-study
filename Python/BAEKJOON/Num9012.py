"""
Date:
  23.02.07
Title:
  BAEKJOON 9012번
Project:
  괄호
Level:
  Silver 4
Name:
  thelight0804
"""
standard_input = """6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()("""

#input test
test = int(input())

for _ in range(test):
  #input PS
  ps = input()
  cnt = 0

  for i in ps:
    if i == '(':
      cnt += 1
    else:
      cnt -= 1
      if(cnt < 0): #invalid PS
        break
  
  if cnt == 0:
    print("YES")
  else:
    print("NO")

""" use stack
for _ in range(test):
  #input PS
  ps = input()
  stack = []

  for i in ps:
    if(i == '('): #stack Push
      stack.append(i)
    elif(len(stack) != 0 and stack[-1] == '('):
      #stack Pop
      stack.pop()
    else:
      #Push ')' and invalid PS
      stack.append(i)
      break

  #output result
  if(len(stack) == 0):
    print("YES")
  else:
    print("NO")
"""