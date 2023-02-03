"""
Date:
  23.01.30
Title:
  BAEKJOON 1316번
Project:
  그룹 단어 체커
Level:
  Silver 5
Name:
  thelight0804
"""
standard_input = """3
happy
new
year"""

#input test case and words
test = int(input())

cnt = 0

for _ in range(test):
  #input word
  word = input()
  same = 0 #count of same word character and cut word character

  for i in range(len(word)-1):
    #cut word different from next character
    if(word[i] != word[i+1]):
      cutWord = word[i+1:] #create new cut word
      same += cutWord.count(word[i])
      if (cutWord.count(word[i]) > 0):
        break
  #group word
  if(same == 0):
    cnt += 1

print(cnt)