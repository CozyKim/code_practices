import sys

input = sys.stdin.readline

n = int(input())
wine = [0] * (n+1)
for i in range(1, n+1):
    wine[i] = int(input())

answer = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        answer[i] = wine[1]
    elif i == 2:
        answer[i] = wine[1] + wine[2]
    else:
        answer[i] = max(answer[i-2] + wine[i], answer[i-3] +
                        wine[i-1] + wine[i], answer[i-1])

print(answer[n])


# n까지 왔을 때 최댓값을 기준으로 계속 이어나간다
