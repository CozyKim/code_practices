# https://www.acmicpc.net/problem/16922

N = int(input())
dp = [set() for _ in range(N + 1)]
dp[1] |= {1, 5, 10, 50}
for i in range(1, N + 1):
    for j in (1, 5, 10, 50):
        for num in dp[i - 1]:
            dp[i].add(num + j)
print(len(dp[N]))
