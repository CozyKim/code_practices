"""
규칙 
    1. 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
    2. 거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.
    3. 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

맨해튼 거리
    두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, 
    T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.

제한 사항
    places의 행 길이(대기실 개수) = 5
    places의 각 행은 하나의 대기실 구조를 나타냅니다.
    places의 열 길이(대기실 세로 길이) = 5
    places의 원소는 P,O,X로 이루어진 문자열입니다.
    places 원소의 길이(대기실 가로 길이) = 5
    P는 응시자가 앉아있는 자리를 의미합니다.
    O는 빈 테이블을 의미합니다.
    X는 파티션을 의미합니다.
    입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.
    return 값 형식
    1차원 정수 배열에 5개의 원소를 담아서 return 합니다.
    places에 담겨 있는 5개 대기실의 순서대로, 거리두기 준수 여부를 차례대로 배열에 담습니다.
    각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.
"""


from collections import deque


def solution(places):

    answer = []
    for place in places:
        visited = [[0 for _ in range(5)] for _ in range(5)]
        flag = 1
        num = 0
        while flag and num < 25:
            i, j = divmod(num, 5)
            if place[i][j] != "P":
                num += 1
                continue
            if bfs(i, j, visited, place) == 0:
                answer.append(0)
                flag = 0
            num += 1
        if flag:
            answer.append(1)
    return answer


def bfs(i, j, visited, place):
    visited[i][j] = 1
    q = deque([(i, j, 0)])
    while q:
        x, y, cnt = q.popleft()
        if cnt == 2:
            continue
        for dx, dy in [[-1, 0], [0, 1], [0, -1], [1, 0]]:
            if 0 <= y + dy < 5 and 0 <= x + dx < 5 and not visited[x + dx][y + dy]:
                if place[x + dx][y + dy] == "P":
                    return 0
                elif place[x + dx][y + dy] == "O":
                    visited[x + dx][y + dy] = 1
                    if cnt + 1 != 2:
                        q.append((x + dx, y + dy, cnt + 1))
                elif place[x + dx][y + dy] == "X":
                    visited[x + dx][y + dy] = 1
    return 1


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
