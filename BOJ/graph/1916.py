# https://www.acmicpc.net/problem/1916
from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

edges = defaultdict(list)
for _ in range(M):
    s, e, cost = map(int, input().split())
    edges[s].append([e, cost])

start, end = map(int, input().split())


def dij(start, end):
    h = [[1, start]]
    costs = defaultdict(int)
    while h:
        cost, node = heapq.heappop(h)
        if costs[node]:
            continue
        costs[node] = cost
        if node == end:
            return cost - 1
        for next_node, edge_cost in edges[node]:
            heapq.heappush(h, [cost + edge_cost, next_node])


print(dij(start, end))
