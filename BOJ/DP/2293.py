# https://www.acmicpc.net/problem/2293

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n
for i in range(n):
    coins[i] = int(input())
coins.sort()
dp = [0] * (k + 1)
# for i in range(n):
#     dp[coins[i]] = 1
dp[0] = 1
for i in range(n):
    for j in range(coins[i], k + 1):
        if j - coins[i] >= 0:
            dp[j] += dp[j - coins[i]]
# print(dp)
print(dp[k])
