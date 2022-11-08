"""
Date:
    22.07.12
Title:
    BAEKJOON 1259번
Project:
    팰린드롬수
Level:
    Bronze 1
Name:
    thelight0804
"""
while(True):
    #수 입력
    inputNum = input()

    #숫자 자리 수 마다 분리
    listNum = list(map(int, str(inputNum)))

    #프로그램 종료 조건
    if inputNum == "0":
        break
    else:
        #팰린드롬수 계산
        palind = False
        for i in range(len(listNum)):
            if listNum[i] == listNum[len(listNum)-i-1]:
                palind = True
            else:
                palind = False
                break

        #팰린드롬수 결과 출력
        if palind is True:
            print("yes")
        else:
            print("no")