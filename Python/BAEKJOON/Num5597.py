"""
Date:
    22.10.28
Title:
    BAEKJOON 5597번
Project:
    未提出者は誰だ
    과제 안 내신 분..?
Level:
    Bronze 5
Name:
    thelight0804
"""
import sys

#input
student = [int(sys.stdin.readline()) for i in range(28)]
index = 0

#list sort
student.sort()

#check student
for i in range(1, 31):
  try:
    index = student.index(i)
  except ValueError:
    print(i, end=' ')