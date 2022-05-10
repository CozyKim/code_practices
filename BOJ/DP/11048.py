# https://www.acmicpc.net/problem/11048

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]
for i in range(N):
    for j in range(M):
        if 0 <= i - 1 and 0 <= j - 1:
            dp[i][j] = max(
                dp[i][j],
                maze[i][j] + dp[i - 1][j - 1],
                maze[i][j] + dp[i - 1][j],
                maze[i][j] + dp[i][j - 1],
            )
        elif 0 <= i - 1:
            dp[i][j] = max(dp[i][j], maze[i][j] + dp[i - 1][j])
        elif 0 <= j - 1:
            dp[i][j] = max(dp[i][j], maze[i][j] + dp[i][j - 1])
print(dp[N - 1][M - 1])
