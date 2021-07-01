# https://www.acmicpc.net/problem/17836

# 벽뚫고 복표지점 가기와 비슷한 내용 -> DP & BFS 이용

import sys
from collections import deque
input = sys.stdin.readline
arr = []
N, M, T = list(map(int, input().split()))
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(2)]


def BFS():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 0
    while q:
        sword, x, y = q.popleft()
        for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if 0 <= nx < N and 0 <= ny < M:
                if sword and visited[1][nx][ny] == -1:
                    visited[1][nx][ny] = visited[1][x][y] + 1
                    q.append([1, nx, ny])

                elif not sword and visited[0][nx][ny] == -1 and arr[nx][ny] != 1:
                    if arr[nx][ny] == 2:
                        visited[1][nx][ny] = visited[0][x][y] + 1
                        q.append([1, nx, ny])
                    else:
                        visited[0][nx][ny] = visited[0][x][y] + 1
                        q.append([0, nx, ny])


BFS()
ans1, ans2 = visited[0][N-1][M-1], visited[1][N-1][M-1]
answer = []
for i in [ans1, ans2]:
    if i != -1 and i <= T:
        answer += [i]
if answer:
    print(min(answer))
else:
    print("Fail")
