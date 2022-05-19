import sys

input = sys.stdin.readline
inputs = []
while True:
    try:
        inputs.append(list(map(int, input().split())))
    except:
        break
dp = [
    [[0 for _ in range(15 + 1)] for _ in range(15 + 1)] for _ in range(len(inputs) + 1)
]

for i in range(len(inputs)):
    for w in range(15 + 1):
        for b in range(15 + 1):
            if w + 1 <= 15:
                dp[i + 1][w + 1][b] = max(
                    dp[i + 1][w + 1][b], dp[i][w][b] + inputs[i][0]
                )
            if b + 1 <= 15:
                dp[i + 1][w][b + 1] = max(
                    dp[i + 1][w][b + 1], dp[i][w][b] + inputs[i][1]
                )
            dp[i + 1][w][b] = max(dp[i + 1][w][b], dp[i][w][b])
print(dp[len(inputs)][15][15])
