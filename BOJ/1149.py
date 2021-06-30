# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0, 0, 0]] * N
dp[0] = [arr[0][0], arr[0][1], arr[0][2]]
for i in range(1, N):
    red = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    green = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    blue = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
    dp[i] = [red, green, blue]


print(min(dp[N-1]))
