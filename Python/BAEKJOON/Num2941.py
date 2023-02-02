"""
Date:
  23.02.02
Title:
  BAEKJOON 2941번
Project:
  크로아티아 알파벳
Level:
  Silver 5
Name:
  thelight0804
"""
standard_input = """dz=ak"""
# 2

#croatia list
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

#input word
word = input()

# find croatia
for j in croatia:
    word = word.replace(j, 'A')

# # find croatia
# for j in range(len(croatia)):
#   if(croatia[j] in word):
#     # replace croatia character to A
#     word = word.replace(croatia[j], 'A')

print(len(word))