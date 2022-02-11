# https://www.acmicpc.net/problem/1167

import sys
import heapq
from collections import defaultdict

V = int(input())

# 간선의 정보 : 점점번호 정점까지거리
graph = defaultdict(list)
input = sys.stdin.readline


for _ in range(V):
    line = list(map(int, input().split()))
    for j in range(1, len(line), 2):
        if line[j] == -1:
            break
        graph[line[0]].append((line[j], line[j + 1]))

print(graph)


def dijkstra(node):
    # Q : (cost, node)
    Q = [(0, node)]
    dist = [1] * (V + 1)
    min_diam = 0
    visited = -1
    while Q:
        diam, now = heapq.heappop(Q)
        if dist[now] == 1:
            dist[now] = diam

            for v, w in graph[now]:
                next_diam = diam - w
                heapq.heappush(Q, (next_diam, v))
            if min_diam > diam:
                min_diam = diam
                visited = now

    return min_diam, visited


def dfs(src):
    stack = [(src, 0)]
    visited = [0 for _ in range(V + 1)]
    visited[src] = 1
    max_wight = 0
    edge_node = -1
    while stack:
        node, wight = stack.pop()
        for v, w in graph[node]:
            if not visited[v]:
                visited[v] = 1
                stack.append((v, wight + w))
                if max_wight < wight + w:
                    max_wight = wight + w
                    edge_node = v

    return max_wight, edge_node


max_diam = 0

node = 1
for _ in range(2):
    diam, node = dijkstra(node)
print(-diam)

for _ in range(2):
    diam, node = dfs(node)
print(diam)

# 속도는 dfs로 푸는 것이 더 빨랐다.
