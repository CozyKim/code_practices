# https://www.acmicpc.net/problem/14499

import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

dice = [0] * 6  # 하늘, 바닥, 상, 하, 좌, 우


def roll_dice(dir):
    global dice
    if dir == 1:  # 오른쪽 이동
        dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]

    elif dir == 2:  # 왼쪽 이동
        dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]

    elif dir == 3:  # 위로 이동
        dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]

    elif dir == 4:  # 아래로 이동
        dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]


direction_map = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

for dir in order:
    dx, dy = direction_map[dir]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < M:
        roll_dice(dir)
        if MAP[nx][ny]:
            dice[1], MAP[nx][ny] = MAP[nx][ny], 0
        else:
            MAP[nx][ny] = dice[1]
        print(dice[0])
        x, y = nx, ny
