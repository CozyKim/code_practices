# https://www.acmicpc.net/problem/23288

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]


def get_count(x, y, visited):
    if visited[x][y]:
        return
    visited[x][y] = 1
    cnt = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and MAP[x][y] == MAP[nx][ny]:
                cnt += get_count(nx, ny, visited)
    return cnt + 1


def get_score(x, y):
    B = MAP[x][y]
    visited = [[0] * M for _ in range(N)]
    cnt = get_count(x, y, visited)
    return B * cnt


direction_map = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
dice_dir = 0
dice_info = [1, 6, 2, 5, 4, 3]  # 위, 아래, 상, 하 , 좌, 우


def rotate_dice(dice_info, direction):
    if direction == 0:
        dice_info = [
            dice_info[4],
            dice_info[5],
            dice_info[2],
            dice_info[3],
            dice_info[1],
            dice_info[0],
        ]
    elif direction == 1:
        dice_info = [
            dice_info[2],
            dice_info[3],
            dice_info[1],
            dice_info[0],
            dice_info[4],
            dice_info[5],
        ]
    elif direction == 2:
        dice_info = [
            dice_info[5],
            dice_info[4],
            dice_info[2],
            dice_info[3],
            dice_info[0],
            dice_info[1],
        ]
    elif direction == 3:
        dice_info = [
            dice_info[3],
            dice_info[2],
            dice_info[0],
            dice_info[1],
            dice_info[4],
            dice_info[5],
        ]
    return dice_info


answer = 0
x, y = 0, 0
for _ in range(K):
    dx, dy = direction_map[dice_dir]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < M):
        dice_dir = (dice_dir + 2) % 4
        dx, dy = direction_map[dice_dir]
        nx, ny = x + dx, y + dy
    answer += get_score(nx, ny)
    dice_info = rotate_dice(dice_info, dice_dir)
    if dice_info[1] > MAP[nx][ny]:
        dice_dir = (dice_dir + 1) % 4
    elif dice_info[1] < MAP[nx][ny]:
        dice_dir = dice_dir - 1 if dice_dir - 1 >= 0 else dice_dir + 3
    x, y = nx, ny
print(answer)
