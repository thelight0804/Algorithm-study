"""
Date:
  22.11.13
Title:
  BAEKJOON 3052번
Project:
  나머지
Level:
  Bronze 2
Name:
  thelight0804
"""

#input num
a = [int(input()) for i in range (10)]
remain = []

for i in range(10):
  temp = a[i] % 42
  #find same div remain
  try:
    remain.index(temp)
  #append div remain when not value
  except ValueError:
    remain.append(temp)

print(len(remain))

"""
#input num
a = [int(input()) for i in range (10)]
arr = []

#input div remain to arr
for i in range(10):
  arr.append(a[i] % 42)

#set array
remain = set(arr)

print(len(remain))
"""