# https://www.acmicpc.net/problem/2206

# 처음에 ansewr = -1 로 초기화
# bfs 에 상하좌우 4개 넣기 (단, 방문한 곳 x)
# 1의 카운트가 2 이상이면 바로 삭제
import sys
from collections import deque
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
_arr = []
for i in range(N):
    _arr.append(list(input().rstrip()))
global tmp
tmp = float('inf')


def bfs(_x, _y, _cnt=0, visited=[[[False] * M for _ in range(N)] for _ in range(2)]):
    queue = deque([(_x, _y, _cnt, 1)])
    visited[0][0][0] = True
    while queue:
        x, y, cnt, leng = queue.popleft()
        if (x, y) == (N-1, M-1):
            return leng

        for next_x, next_y in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
            if (0 <= next_x < N) and (0 <= next_y < M):
                if cnt == 1:
                    if visited[1][next_x][next_y] or _arr[next_x][next_y] == '1':
                        continue
                    visited[1][next_x][next_y]
                    queue.append([next_x, next_y, 1, leng + 1])
                else:
                    if visited[0][next_x][next_y]:
                        continue
                    visited[int(_arr[next_x][next_y]) - 0
                            ][next_x][next_y] = True
                    queue.append([next_x, next_y, int(
                        _arr[next_x][next_y]) - 0, leng + 1])
        # if cnt == 0:
        #     if (x, y) not in visited[0]:
        #         visited[0].append((x, y))
        #             if (0 <= next_x < N) and (0 <= next_y < M):
        #                 if (next_x, next_y) in visited[0]:
        #                     continue
        #                 elif _arr[next_x][next_y] == '1':
        #                     queue.append([next_x, next_y, cnt + 1, leng + 1])
        #                 elif _arr[next_x][next_y] == '0':
        #                     queue.append([next_x, next_y, cnt, leng + 1])

        # elif cnt == 1:
        #     if (x, y) not in visited[1]:
        #         visited[1].append((x, y))
        #         for next_x, next_y in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        #             if (0 <= next_x < N) and (0 <= next_y < M):
        #                 if (next_x, next_y) in visited[1]:
        #                     continue
        #                 elif _arr[next_x][next_y] == '0':
        #                     queue.append([next_x, next_y, cnt, leng + 1])

    return -1


print(bfs(0, 0))


# if tmp == float('inf'):
#     print(-1)
# else:
#     print(tmp)
