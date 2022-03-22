# https://www.acmicpc.net/problem/12100

import sys, copy

N = int(input())
input = sys.stdin.readline
table = []
first_max_block = -1
for _ in range(N):
    line = list(map(int, input().split()))
    first_max_block = max(first_max_block, max(line))
    table.append(line)

map_direction = {
    "R": (0, -1, N - 1),
    "L": (0, 1, 0),
    "U": (1, 0, 0),
    "D": (-1, 0, N - 1),
}


def change_block(raw, column, dircetion, table):
    global N
    if dircetion == "R":
        for idx in range(column, -1, -1):
            if table[raw][idx]:
                table[raw][idx], table[raw][column] = (
                    table[raw][column],
                    table[raw][idx],
                )
                break
    if dircetion == "L":
        for idx in range(column, N):
            if table[raw][idx]:
                table[raw][idx], table[raw][column] = (
                    table[raw][column],
                    table[raw][idx],
                )
                break
    if dircetion == "U":
        for idx in range(raw, N):
            if table[idx][column]:
                table[idx][column], table[raw][column] = (
                    table[raw][column],
                    table[idx][column],
                )
                break
    if dircetion == "D":
        for idx in range(raw, -1, -1):
            if table[idx][column]:
                table[idx][column], table[raw][column] = (
                    table[raw][column],
                    table[idx][column],
                )
                break


def dfs(direction, max_block, cnt, table):
    global N
    if cnt == 5:
        return max_block
    if direction in "RL":
        for r in range(N):
            mapping = map_direction[direction]  # r,c,first_c
            stop_flag = False
            merge_list = []
            c = mapping[2]
            while not stop_flag:
                if N - 1 < c or c < 0:
                    break
                change_block(r, c, direction, table)
                if table[r][c] == 0:
                    break
                if c == mapping[2]:
                    c += mapping[1]
                    continue
                if (
                    table[r][c] == table[r][c - mapping[1]]
                    and (r, c - mapping[1]) not in merge_list
                ):
                    table[r][c - mapping[1]] *= 2
                    table[r][c] = 0
                    change_block(r, c, direction, table)
                    max_block = max(max_block, table[r][c - mapping[1]])
                    merge_list.append((r, c - mapping[1]))
                c += mapping[1]
    elif direction in "UD":
        for c in range(N):
            mapping = map_direction[direction]  # r,c,first_c
            stop_flag = False
            merge_list = []
            r = mapping[2]
            while not stop_flag:
                if N - 1 < r or r < 0:
                    break
                change_block(r, c, direction, table)

                if table[r][c] == 0:
                    break
                if r == mapping[2]:
                    r += mapping[0]
                    continue
                if (
                    table[r][c] == table[r - mapping[0]][c]
                    and (r - mapping[0], c) not in merge_list
                ):
                    table[r - mapping[0]][c] *= 2
                    table[r][c] = 0
                    change_block(r, c, direction, table)

                    max_block = max(max_block, table[r - mapping[0]][c])
                    merge_list.append((r - mapping[0], c))
                r += mapping[0]

    tmp = []
    for d in "RLUD":
        tmp.append(dfs(d, max_block, cnt + 1, copy.deepcopy(table)))
    return max(tmp)


answer = []
for d in "RLUD":
    answer.append(dfs(d, first_max_block, 0, copy.deepcopy(table)))
print(max(answer))


## 다른 사람 풀이
from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer, q = 0, deque()


def get(i, j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j] = 0


def merge(i, j, di, dj):
    while q:
        x = q.popleft()
        if not board[i][j]:
            board[i][j] = x
        elif board[i][j] == x:
            board[i][j] = x * 2
            i, j = i + di, j + dj
        else:
            i, j = i + di, j + dj
            board[i][j] = x


def move(k):
    if k == 0:
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(n):
            for i in range(n - 1, -1, -1):
                get(i, j)
            merge(n - 1, j, -1, 0)
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                get(i, j)
            merge(i, n - 1, 0, -1)


def solve(count):
    global board, answer
    if count == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return
    b = [x[:] for x in board]

    for k in range(4):
        move(k)
        solve(count + 1)
        board = [x[:] for x in b]


solve(0)
print(answer)

# 나와의 비교 :
# 나는 for 문을 통해서 무식하게 이동시켰지만 이 분은 큐를 이용해서 저장했다가 풀어 놓는 방식으로 푸셨다.
# 좋은 방법이니 잘 기억해 두자
