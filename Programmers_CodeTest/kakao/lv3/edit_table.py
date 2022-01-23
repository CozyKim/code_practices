# https://programmers.co.kr/learn/courses/30/lessons/81303

"""
문제 설명
    명령어를 기반으로 표의 행을 선택, 삭제, 복구하는 프로그램 작성과제 맡음
    파란색으로 칠해진 칸은 현재 선택된 항

명령어
    "U X" : 현재 선택된 행에서 X칸 위에 있는 행 선택
    "D X" : 현재 선택된 행에서 X칸 아래에 있는 행을 선택
    "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행 선택. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗행을 선택
    "Z" : 가장 최근에 삭제된 행을 원래대로 복구. 단, 현재 선택된 행은 바뀌지 않음

    
조건 
    한 번에 한 행만 선택할 수 있다
    선택된 항은 표의 범위를 벗어 날 수 없다.

입력
    n : 처음 표의 행의 개수를 나타내는 정수
    k : 처음에 선택된 행의 위치를 나타내는 정수
    cmd : 수행한 명령어들이 담긴 문자열 배열

출력
    OX : 모든 명령어를 수행한 후 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X
"""


def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]

    # 현재 위치를 나타내는 변수 now
    now = k

    # 사용 했던 로그를 담는 stack 이 필요(클리어 할 때마다 위치 저장)
    stack = []

    for c in cmd:
        CMD = c.split()[0]
        if CMD == "U":
            now -= int(c.split()[1])

        elif CMD == "D":
            now += int(c.split()[1])

        elif CMD == "C":
            stack.append(now)
            answer.pop()
            if now == len(answer):
                now -= 1
        elif CMD == "Z":
            prev = stack.pop()
            answer.append("O")
            if prev <= now:
                now += 1

    while stack:
        prev = stack.pop()
        answer.insert(prev, "X")

    answer = "".join(answer)

    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
