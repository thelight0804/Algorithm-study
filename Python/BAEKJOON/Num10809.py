"""
Date:
    22.11.03
Title:
    BAEKJOON 10809번
Project:
    알파벳 찾기
Level:
    Bronze 5
Name:
    thelight0804
"""
# standard_input="baekjoon"


#initial alphabet location
alphabet = [-1 for i in range(26)]

#input string
str = input()

asc = 0 #ascii number
count = 0 #str location

#save str location to ascii number
for i in str:
  asc = ord(i) - 97
  if alphabet[asc] == -1:
    alphabet[asc] = count
  count += 1

#print result
for i in range(len(alphabet)):
  print(alphabet[i], end=" ")

"""
#input string
str = input()

#inital alphbet list to ascii
alphabet = list(range(97, 123))

for i in alphabet:
  print(str.find(chr(i)), end = ' ')
"""