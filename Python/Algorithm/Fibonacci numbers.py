"""
Date:
    2022.08.25
Title:
    피보나치 수열
Project:
    Dynamic Programming
"""

#Not used memoization
# def fibo(x):
#   #1과 2는 1이 된다
#   if x == 1: return 1
#   if x == 2: return 1
#   return fibo(x - 1) + fibo(x - 2)

# num = int(input())
# print(fibo(num))

##########

#Used memoization
d = [0] * 100 #memoization

def fibo2(x):
  if x == 1: return 1
  if x == 2: return 1
  #이미 구한 값이면 해당 값을 return 한다
  if d[x] != 0: return d[x]
  else: d[x] = fibo2(x - 1) + fibo2(x - 2)
  return d[x]

num = int(input())
print(fibo2(num))