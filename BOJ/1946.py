import sys

cnt = 1
scores = []
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    for _ in range(N):
        scores.append(list(map(int, sys.stdin.readline().split())))
    scores.sort()
    min = scores[0][1]
    for i in range(1, N):
        if scores[i][1] < min:
            cnt += 1
            min = scores[i][1]
    print(cnt)

    cnt = 1
    scores = []
