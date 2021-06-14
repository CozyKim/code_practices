# https://www.acmicpc.net/problem/13023
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = {}
tmp = []
for _ in range(M):
    _a, _b = map(int, input().split())
    tmp.append(_a)
    tmp.append(_b)
    for a, b in [[_a, _b], [_b, _a]]:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

_start = [[i, tmp.count(i)] for i in tmp]
start = [i for i, v in _start if v == min(_start, key=lambda x:x[1])[1]]
answer = 0

tmp = []
visited = []
stack = [start[0]]
cnt = 1
while stack:
    n = stack.pop()
    if cnt == 5:
        answer = 1
        break
    if n not in visited:
        visited.append(n)
        stack += set(graph[n]) - set(visited)

        cnt += 1
# print(visited)
# if max(tmp) == N:
#     answer = 1
print(answer)
