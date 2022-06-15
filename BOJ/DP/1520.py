# https://www.acmicpc.net/problem/1520

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]


def dfs(r, c):
    global answer, dp
    if (r, c) == (M - 1, N - 1):
        dp[r][c] = 1
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 0
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N:
            if board[nr][nc] < board[r][c]:
                dp[r][c] += dfs(nr, nc)

    return dp[r][c]


print(dfs(0, 0))
