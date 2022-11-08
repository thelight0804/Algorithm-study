"""
Date:
    22.07.24
Title:
    BAEKJOON 10814번
Project:
    나이순 정렬
Level:
    Bronze 1
Name:
    thelight0804
"""
# a = "74759336" #전화 번호 A
# b = "36195974" #전화 번호 B
a = input()
b = input()
num = "" #더한 값
sum = ""

# A와 B 교차로 더하기
for i in range(len(a)):
  num += a[i] + b[i]

while(True):
  # 남은 숫자가 2개인 경우
  if(len(num) == 2):
    print(num) #결과 출력
    break;
  else:
    for i in range(1, len(num)):
      #두 수를 더한 값에 1의 자리를 더한다
      sum += str(int(num[i]) + int(num[i-1])).zfill(2)[1]
  num = sum #num 갱신
  sum = "" #sum 초기화