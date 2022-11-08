"""
Date:
    22.07.05
Title:
    BAEKJOON 10250번
Project:
    ACM 호텔
Level:
    Bronze 3
Name:
    thelight0804
"""
#반복 횟수 입력
roopNum = 0
roopNum = int(input())

for i in range(roopNum):
  #층 수, 각 층의 방 수, 손님 번호 입력
  str = input()
  strList = [int(i) for i in str.split(' ')]
  h = strList[0] #층 수
  w = strList[1] #각 층의 방 수
  guest = strList[2] #손님 번호 입력
  hotel = list() #호텔 List 생성
  
  #호텔 객실 배정
  for i in range(h):
    tmp = [] #2차원 List에 사용
    for j in range(w):
      tmp.append((i+1)*100 + (j+1))
    hotel.append(tmp) #만들어진 List를 List안에 추가
  
  #손님 방 배정
  room = 0 # 방 배정 번호
  count = 0 # 방 순번 카운팅

  for i in range(w):
    for j in range(h):
      count += 1
      if(count == guest):
        room = hotel[j][i]

  #손님 방 출력
  print(room)