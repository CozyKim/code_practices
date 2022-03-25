# https://www.acmicpc.net/problem/1504

from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

N, E = map(int, input().split())
graph = defaultdict(dict)
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost
    graph[b][a] = cost
v1, v2 = map(int, input().split())


def dij(start, end):
    h = [[1, start]]  # cost, node
    min_dist = defaultdict(int)
    while h:
        cost, node = heapq.heappop(h)
        if min_dist[node]:
            continue
        min_dist[node] = cost
        if node == end:
            return cost
        for next_node, next_cost in graph[node].items():
            heapq.heappush(h, [cost + next_cost, next_node])
    return -1


min_cost = float("inf")
for a, b in [(v1, v2), (v2, v1)]:
    x, y, z = dij(1, a), dij(a, b), dij(b, N)
    if x != -1 and y != -1 and z != -1:
        min_cost = min(min_cost, x + y + z - 3)
if min_cost == float("inf"):
    print(-1)
else:
    print(min_cost)
