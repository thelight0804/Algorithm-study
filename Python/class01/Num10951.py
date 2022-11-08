"""
Date:
    22.10.12
Title:
    BAEKJOON 10951번
Project:
    A+B - 4
Level:
    Bronze 5
Name:
    thelight0804
"""
#덧셈 연산 반복
standard_input = """3
1
2
3
"""
while(1):
  try:
    str = input() #두 수 입력

    # 숫자 분리
    strArr = [int(i) for i in str.split(' ')]

    #숫자 출력
    print(strArr[0] + strArr[1])

  #EOF처리에 실패했을 때 프로그램 종료
  except EOFError:
    break