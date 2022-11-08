"""
Date:
    2022.08.17
Title:
    Programmers 알고리즘 문제 해설 3번
Project:
    나머지 한 점
"""
def solution(v):
    answer = []
    x = v[0][0]
    y = v[0][1]
    
    #X가 크고 Y가 작을 때
    for i in range(len(v)):
        tempX = v[i][0]
        tempY = v[i][1]
        if tempX > x:
            x = tempX
        if tempY < y:
            y = tempY
    answer.append([x, y])
    
    #X가 크고 Y가 클 때
    for i in range(len(v)):
        tempX = v[i][0]
        tempY = v[i][1]
        if tempX > x:
            x = tempX
        if tempY > y:
            y = tempY
    answer.append([x, y])
    
    #X가 작고 Y가 클 때
    for i in range(len(v)):
        tempX = v[i][0]
        tempY = v[i][1]
        if tempX < x:
            x = tempX
        if tempY > y:
            y = tempY
    answer.append([x, y])
    
    #X가 작고 Y가 작을 때
    for i in range(len(v)):
        tempX = v[i][0]
        tempY = v[i][1]
        if tempX < x:
            x = tempX
        if tempY < y:
            y = tempY
    answer.append([x, y])
    
    #같은 좌표 제거
    for i in range(len(v)):
        for j in range(len(answer)):
            if v[i] == answer[j]:
                del answer[j]
                break
                
    #list in list remove
    x = answer[0][0]
    y = answer[0][1]
    del answer[0]

    answer.append(x)
    answer.append(y)

    print(answer)
    
    return answer