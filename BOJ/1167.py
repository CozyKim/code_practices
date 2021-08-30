# https://www.acmicpc.net/problem/1167
import sys
from collections import deque
input = sys.stdin.readline
V = int(input())
graph = {}
for _ in range(V):
    tmp = list(map(int, input().split()))
    for idx, i in enumerate(tmp):
        if i == -1:
            break
        if idx % 2 == 1:
            if tmp[0] not in graph:
                graph[tmp[0]] = {i: tmp[idx+1]}
            else:
                graph[tmp[0]][i] = tmp[idx+1]
# print(graph)


def BFS(root):
    q = deque([(root, 0)])
    visited = []
    max_len = 0
    while q:
        n, length = q.popleft()
        max_len = max(max_len, length)
        if n not in visited:
            visited.append(n)
            for k in graph[n].keys():
                if k not in visited:
                    q.append((k, length + graph[n][k]))
    return visited, max_len


def DFS(root):
    stack = [(root, 0)]
    visited = []
    max_len = 0
    while stack:
        point, leng = stack.pop()
        max_len = max(max_len, leng)
        if point not in visited:
            visited.append(point)
            for k in graph[point].keys():
                if k not in visited:
                    stack.append((k, leng + graph[point][k]))
    return visited, max_len


check = set(range(1, V+1))
last_maxlen = 0
# while check:
# for check in range(1, V+1):
visited, maxlen = DFS(list(check)[0])
# diameter = max(maxlen, last_maxlen)
# check -= set(visited)
# last_maxlen = maxlen
print(maxlen)
