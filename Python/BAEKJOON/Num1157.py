"""
Date:
  22.11.17
Title:
  BAEKJOON 1157번
Project:
  단어 공부
Level:
  Bronze 1
Name:
  thelight0804
"""
# standard_input='Mississipi'

#input String
word = input()

#convert uppercase
word = word.upper()

#set word list
setWord = list(set(word))

#alphabet count
cnt = []

#count word alphabet
for i in setWord:
  cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
  print('?')
else:
  index = cnt.index(max(cnt))
  print(setWord[index])