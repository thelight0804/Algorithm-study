"""
Date:
  23.02.19
Title:
  BAEKJOON 1158번
Project:
  요세푸스 문제
Level:
  Silver 4
Name:
  thelight0804
"""
standard_input = """7 3"""
#<3, 6, 2, 7, 5, 1, 4>

n, k = map(int, input().split())

#number queue
q = [i for i in range(1, n+1)]
l = [] #Josephus result list
index = 0 #pop index to q

for i in range(n):
  #add pop index
  index += k-1
  if index >= len(q):
    #return back queue
    index %= len(q)
  #add Josephus number
  l.append(str(q.pop(index)))

#output result
print("<" + ", ".join(l) + ">")