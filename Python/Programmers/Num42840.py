"""
Date:
  23.04.03
Problem:
  Programmers 42840
Project:
  모의고사
Level:
  Lv. 1
Author:
  thelight0804
"""


def solution(answers):
  answer = []

  # 찍는 방식
  per1 = [1, 2, 3, 4, 5]
  per2 = [2, 1, 2, 3, 2, 4, 2, 5]
  per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

  # 정답 개수
  score = [0] * 3

  # Brute force
  for i in range(len(answers)):
      if per1[i % len(per1)] == answers[i]:
          score[0] += 1
      if per2[i % len(per2)] == answers[i]:
          score[1] += 1
      if per3[i % len(per3)] == answers[i]:
          score[2] += 1

  # 가장 많은 문제를 맞춘 사람
  for i, value in enumerate(score):
      if value == max(score):
          answer.append(i+1)

  return answer
