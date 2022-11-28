"""
Date:
  22.11.28
Title:
  BAEKJOON 4673번
Project:
  셀프 넘버
Level:
  Silver 5
Name:
  thelight0804
"""
# numList = [1, 2, 3 ... 9999, 10000]
numList = list(range(1, 10000))

# roop 1 ~ 10000
for i in range(1, 10000):
  a = list(map(int, str(i)))
  # num = digit sum
  num = i + sum(a)
  try:
    # remove digit sum
    numList.remove(num)
  except:
    pass

#print result
for i in range(len(numList)):
  print(numList[i])