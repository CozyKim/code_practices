# https://www.acmicpc.net/problem/14890

import sys

input = sys.stdin.readline

N, L = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]


def possible_put_slope(pos, direction, height):
    global L, N
    x, y = pos
    dx, dy = direction
    cnt = 1
    check = x if dx else y
    while 0 <= x < N and 0 <= y < N:
        if MAP[x][y] != height:
            return False
        if SLOPE[check]:
            return False
        if cnt == L:
            return True
        x, y = x + dx, y + dy
        check = x if dx else y
        cnt += 1
    return False


answer = 0

direction_map = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

# 가로
for i in range(N):
    SLOPE = [0] * N
    for j in range(N - 1):
        if MAP[i][j] - MAP[i][j + 1] == 1:
            if possible_put_slope((i, j + 1), direction_map["R"], MAP[i][j + 1]):
                for y in range(j + 1, j + 1 + L):
                    SLOPE[y] = 1
            else:
                break
        elif MAP[i][j] - MAP[i][j + 1] == -1:
            if possible_put_slope((i, j), direction_map["L"], MAP[i][j]):
                for y in range(j - L + 1, j + 1):
                    SLOPE[y] = 1
            else:
                break
        elif MAP[i][j] == MAP[i][j + 1]:
            continue
        else:
            break
    else:
        answer += 1

# 세로
for j in range(N):
    SLOPE = [0] * N
    for i in range(N - 1):
        if MAP[i][j] - MAP[i + 1][j] == 1:
            if possible_put_slope((i + 1, j), direction_map["D"], MAP[i + 1][j]):
                for y in range(i + 1, i + 1 + L):
                    SLOPE[y] = 1
            else:
                break
        elif MAP[i][j] - MAP[i + 1][j] == -1:
            if possible_put_slope((i, j), direction_map["U"], MAP[i][j]):
                for y in range(i - L + 1, i + 1):
                    SLOPE[y] = 1
            else:
                break
        elif MAP[i][j] == MAP[i + 1][j]:
            continue
        else:
            break
    else:
        answer += 1
print(answer)
