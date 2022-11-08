"""
Date:
    2022.10.06
Title:
    Programmers 알고리즘 문제 해설 6번
Project:
    스티커 모으기
"""
def solution(sticker):
    #스티커가 단 하나일 때
    if len(sticker) == 1:
        return sticker[0]
    
    dp1 = [0] * len(sticker)
    dp2 =  [0] * len(sticker)
    
    #첫 번째 스티커를 뜯는 경우
    dp1[0] = sticker[0] #값 부여
    dp1[1] = dp1[0] #두 번째 스티커는 떼지 못한다
    for i in range(2, len(sticker) -1):
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])
    
    #첫 번째 스티커를 뜯지 않는 경우
    for i in range(1, len(sticker)):
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])
    
    answer = max(dp1[-2], dp2[-1])
    #dp1[-1], dp2[0]은 불가능
    
    return answer