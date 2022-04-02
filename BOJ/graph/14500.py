# https://www.acmicpc.net/problem/14500

# 종류 5가지, 회전 대칭 가능, 하나를 적절히 놓아서 놓인 칸 안에 쓰여있는 수들의 합을 최대로 하는 프로그램

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))
answer = -1

visited = [[0] * M for _ in range(N)]

max_node_value = max(map(max, table))


def dfs(node, sum_num, cnt, visited_nodes):
    global answer, visited
    if cnt == 4:
        answer = max(answer, sum_num)
        return

    if sum_num + max_node_value * (4 - cnt) < answer:
        return

    for xx, yy in visited_nodes:
        x = xx
        y = yy

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < N and 0 <= y + dy < M:
                if not visited[x + dx][y + dy]:
                    visited[x + dx][y + dy] = 1
                    dfs(
                        (x + dx, y + dy),
                        sum_num + table[x + dx][y + dy],
                        cnt + 1,
                        visited_nodes + [(x + dx, y + dy)],
                    )
                    visited[x + dx][y + dy] = 0


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs((i, j), table[i][j], 1, [(i, j)])
        visited[i][j] = 0
print(answer)
