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

# 삭제 pop, 되돌리기 insert -> 전에 풀이 : 실패

# 연결리스트 처럼 구현
def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]

    # 초기화
    table = [[i - 1, i, i + 1] for i in range(n)]
    table[n - 1][2] = "-1"
    table[0][0] = "-1"

    stack = []

    for CMD in cmd:
        if CMD[0] == "U":
            for _ in range(int(CMD[2:])):
                k = table[k][0]
        elif CMD[0] == "D":
            for _ in range(int(CMD[2:])):
                k = table[k][2]
        elif CMD[0] == "C":
            stack.append(table[k])
            if table[k][2] == "-1":
                k = table[k][0]
                table[k][2] = "-1"

            elif table[k][0] == "-1":
                k = table[k][2]
                table[k][0] = "-1"

            else:
                table[table[k][0]][2] = table[k][2]
                table[table[k][2]][0] = table[k][0]
                k = table[k][2]
        elif CMD[0] == "Z":
            last_del = stack.pop()
            if last_del[2] == "-1":
                table[last_del[0]][2] = last_del[1]
            elif last_del[0] == "-1":
                table[last_del[2]][0] = last_del[1]
            else:
                table[last_del[0]][2] = last_del[1]
                table[last_del[2]][0] = last_del[1]

    for _, i, _ in stack:
        answer[i] = "X"
    print(table)
    print(stack)
    return "".join(answer)


print(
    solution(
        8,
        0,
        [
            "C",
            "C",
            "C",
            "C",
            "C",
            "C",
            "C",
            "Z",
            "Z",
            "Z",
            "Z",
            "Z",
            "Z",
            "Z",
        ],
    )
)
