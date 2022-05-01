# https://www.acmicpc.net/problem/2096

import sys

input = sys.stdin.readline

N = int(input())
a, b, c = map(int, input().split())
max_dp = [a, b, c]
min_dp = [a, b, c]
for _ in range(N - 1):
    line = list(map(int, input().split()))
    n_max_dp = [-1, -1, -1]
    n_min_dp = [float("inf")] * 3
    for c in range(3):
        for dc in (-1, 0, 1):
            nc = c + dc
            if 0 <= nc < 3:
                n_max_dp[nc] = max(n_max_dp[nc], max_dp[c] + line[nc])
                n_min_dp[nc] = min(n_min_dp[nc], min_dp[c] + line[nc])
    max_dp = n_max_dp[:]
    min_dp = n_min_dp[:]


print(f"{max(max_dp)} {min(min_dp)}")
