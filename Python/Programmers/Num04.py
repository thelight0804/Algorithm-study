"""
Date:
    2022.08.23
Title:
    Programmers 알고리즘 문제 해설 4번
Project:
    가장 큰 정사각형 찾기
"""
def solution(board):
    answer = 0
    
    #board[0]의 예외 처리
    if board[0][0] == 1:
        answer = 1
    
    #2차원 배열 반복
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            #정사각형 찾기
            #오른쪽 아래로 내려가면 list의 범위를 넘어가게 된다
            if board[i][j] != 0:
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) + 1
                #가장 큰 값 저장
                if board[i][j] > answer:
                    answer = board[i][j]
            #정사각형이 하나도 없는 경우
            elif answer == 0 and board[i][j] != 0:
                answer = 1

    #정사각형 넓이
    return answer ** 2