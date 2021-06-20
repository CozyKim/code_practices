# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
input = sys.stdin.readline

cnt_1 = 0
matrix = []
N = int(input())
for i in range(N):
    matrix += [input()]
    cnt_1 += matrix[i].count('1')

houses = []


def move(position):
    if position[0] == 0 and position[1] == 0:
        return [[position[0] + x, position[1] + y] for x, y in [[1, 0], [0, 1]]]

    elif position[0] == 0 and position[1] == N - 1:
        return [[position[0] + x, position[1] + y] for x, y in [[0, -1], [1, 0]]]

    elif position[0] == N - 1 and position[1] == 0:
        return [[position[0] + x, position[1] + y] for x, y in [[-1, 0], [0, 1]]]

    elif position[0] == N - 1 and position[1] == N - 1:
        return [[position[0] + x, position[1] + y] for x, y in [[-1, 0], [0, -1]]]

    elif position[0] == 0:
        return [[position[0] + x, position[1] + y] for x, y in [[1, 0], [0, -1], [0, 1]]]

    elif position[0] == N-1:
        return [[position[0] + x, position[1] + y] for x, y in [[-1, 0], [0, -1], [0, 1]]]

    elif position[1] == 0:
        return [[position[0] + x, position[1] + y] for x, y in [[1, 0], [-1, 0], [0, 1]]]

    elif position[0] == N - 1:
        return [[position[0] + x, position[1] + y] for x, y in [[1, 0], [-1, 0], [0, -1]]]

    else:
        return [[position[0] + x, position[1] + y] for x, y in [[1, 0], [-1, 0], [0, -1], [0, 1]]]


def BFS(root):
    queue = deque([root])
    visited = []
    while queue:
        n = queue.popleft()
        if n not in visited and matrix[n[0]][n[1]] == '1':
            visited.append(n)
            next_position = move(n)
            for x, y in next_position:
                if matrix[x][y] == '1':
                    queue += [[x, y]]
    return visited


start = 0
_visited = []
while cnt_1 > len(_visited):
    if matrix[start//N][start % N] == '1' and [start//N, start % N] not in _visited:
        n = BFS([start//N, start % N])
        _visited += n
        houses.append(len(n))
    else:
        start += 1

print(len(houses))
houses.sort()
for i in houses:
    print(i)

# dfs로 푼 사람 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(input())
houses = [list(map(int, input())) for i in range(N)]
global count
count = 0
apt = []


def dfs(x, y):
    global count
    houses[x][y] = 0
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if houses[nx][ny] == 1:
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if houses[i][j] == 1:
            count = 0
            dfs(i, j)
            apt.append(count)

print(len(apt))
apt.sort()
for i in apt:
    print(i)
