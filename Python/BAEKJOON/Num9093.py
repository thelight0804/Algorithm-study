"""
Date:
  23.02.06
Title:
  BAEKJOON 9093번
Project:
  단어 뒤집기
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input = """2
# I am happy today
# We want to win the first prize"""

#input word
test = int(input())

for _ in range(test):
  #input string
  word = input().split()
  for i in word:
    #output reverse slice
    print(i[::-1], end=" ")
  print("")

#Use stack
"""
for _ in range(test):
  word = input().split() #input String
  for i in range(len(word)):
    for j in range(len(word[i])):
      stack.append(word[i][j]) #push stack
    for j in range(len(stack)):
      print(stack.pop(), end="") #pop stack
    print(" ", end="")
"""