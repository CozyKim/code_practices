# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo

"""
종료 조건
    블랙홀에 빠지거나 시작 지점으로 돌아오면 종료
블록
    1 : 상, 우 바뀜, 나머지는 완전 반대로 변경
    2 : 하, 우 바뀜
    3 : 하, 좌 바뀜
    4 : 상, 좌 바뀜
    5 : 모든 방향에서 와전 반대로 변경
웜홀
    6~10 : 웜홀은 같은 숫자가 적힌 위치로 방향을 유지한채 이동
블랙홀
    -1 : 종료조건
점수 획득 조건
    블록, 벽에 부딪치는 횟수
    웜홀을 통과하는 건 횟수로 안 침

찾아낸 특징
    벽을 부딪칠 경우 부딪치기전 카운트x2 +1 이 최종 결과
"""

direction_map = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}  # 우, 상, 좌, 하


def block_result(block, direction):
    if block == 1:
        if direction == 3:
            return 0
        elif direction == 2:
            return 1
        else:
            return (direction + 2) % 4
    elif block == 2:
        if direction == 1:
            return 0
        elif direction == 2:
            return 3
        else:
            return (direction + 2) % 4

    elif block == 3:
        if direction == 0:
            return 3
        elif direction == 1:
            return 2
        else:
            return (direction + 2) % 4

    elif block == 4:
        if direction == 0:
            return 1
        elif direction == 3:
            return 2
        else:
            return (direction + 2) % 4

    elif block == 5:
        return (direction + 2) % 4


def move_pointer(x, y, dir):
    global blackhole
    cnt = 0
    start = (x, y)
    while 0 <= x < N and 0 <= y < N:
        if board[x][y] == -1:
            return cnt
        if (x, y) == start and cnt:
            return cnt
        if dp[x][y][dir] >= cnt:
            return cnt
        dp[x][y][dir] = cnt
        if 1 <= board[x][y] <= 5:
            prev_dir = dir
            dir = block_result(board[x][y], dir)
            if abs(dir - prev_dir) == 2:
                return cnt * 2 + 1
            cnt += 1
        elif 6 <= board[x][y] <= 10:
            x, y = warmhole[(x, y)]
        dx, dy = direction_map[dir]
        x, y = x + dx, y + dy
    return cnt * 2 + 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    dp = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
    board = []
    tmp = {}
    warmhole = {}
    blackhole = set()
    answer = 0
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if 5 < line[j] <= 10:
                if line[j] in tmp:
                    warmhole[tmp[line[j]]] = (i, j)
                    warmhole[(i, j)] = tmp[line[j]]
                else:
                    tmp[line[j]] = (i, j)
            elif line[j] == -1:
                blackhole.add((i, j))
        board.append(line)
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                for dir in range(4):
                    answer = max(answer, move_pointer(i, j, dir))
    print(f"#{test_case} {answer}")

    # ///////////////////////////////////////////////////////////////////////////////////
