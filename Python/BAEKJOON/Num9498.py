"""
Date:
    22.10.22
Title:
    BAEKJOON 9498번
Project:
    시험 성적
Level:
    Bronze 5
Name:
    thelight0804
"""
score = int(input())

if score <= 101 and score >=90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")