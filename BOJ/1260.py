# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

# 1
# 그래프를 그리는데 node - list로 그래프 구현 / dict를 이용하여 푸는 것이 있다
# 나는 dict를 구하는것이 다인 줄 알았는데 배열로 matrix를 만들어 푸는 방법을 이용해보자

#  dict이용 -> 실패


def BFS(graph, root):
    queue = deque([root])
    visited = []
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += sorted(graph[n])
    return visited


def DFS(graph, root):
    stack = [root]
    visited = []
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += sorted(graph[n], reverse=True)
    return visited


input = sys.stdin.readline
graph = {}
N, M, V = map(int, input().split())
for _ in range(M):
    n, m = map(int, input().split())
    if n not in graph:
        graph[n] = [m]
    else:
        graph[n] = list(set(graph[n]) | set([m]))
    if m not in graph:
        graph[m] = [n]
    else:
        graph[m] = list(set(graph[m]) | set([n]))
# print(graph)
if V not in graph:
    print(V)
else:
    print(*DFS(graph, V))
    print(*BFS(graph, V))


# 2
# matrix -> 성공


input = sys.stdin.readline
graph = {}
N, M, V = map(int, input().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    n, m = map(int, input().split())
    matrix[n][m] = 1
    matrix[m][n] = 1


def DFS(root, visited=[]):
    if root not in visited:
        visited.append(root)
        for i in range(1, N+1):
            if matrix[root][i] == 1:
                DFS(i, visited)
    return visited


def BFS(root):
    queue = deque([root])
    visited = []
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            for i in range(1, N+1):
                if matrix[n][i] == 1:
                    queue.append(i)
    return visited


print(*DFS(V))
print(*BFS(V))
