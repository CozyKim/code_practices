# https://www.acmicpc.net/problem/3190

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

BOARD = [[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    BOARD[r - 1][c - 1] = 1

L = int(input())

ROUTE = deque([])

DICTECTION_MAP = ((0, 1), (1, 0), (0, -1), (-1, 0))
for _ in range(L):
    time, direction = input().split()
    ROUTE.append((int(time), direction))

R, C = 0, 1
cnt = 1
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
dr, dc = 0, 1
time, direction = ROUTE.popleft()
direction_idx = 0
answer = 0
SNAKE = deque([(0, 0)])

while 0 <= R < N and 0 <= C < N:
    if visited[R][C]:
        break
    visited[R][C] = 1
    SNAKE.append((R, C))

    if not BOARD[R][C]:
        tail_r, tile_c = SNAKE.popleft()
        visited[tail_r][tile_c] = 0
    else:
        BOARD[R][C] = 0
    if cnt == time:
        if direction == "L":
            direction_idx -= 1
        else:
            direction_idx += 1
        if direction_idx > 3:
            direction_idx -= 4
        elif direction_idx < 0:
            direction_idx += 4
        dr, dc = DICTECTION_MAP[direction_idx]
        if ROUTE:
            time, direction = ROUTE.popleft()
    cnt += 1
    R += dr
    C += dc

print(cnt)
