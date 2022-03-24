# https://www.acmicpc.net/problem/1238

from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline


def solution():
    N, M, X = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(M):
        a, b, cost = map(int, input().split())
        graph[a].append([b, cost])

    min_costs = defaultdict(int)

    def dji(start, arr=None):
        h = [[1, start]]
        while h:
            cost, node = heapq.heappop(h)
            if min_costs[node]:
                continue
            min_costs[node] = cost
            if arr == node:
                return cost
            for next_node, next_cost in graph[node]:
                heapq.heappush(h, [cost + next_cost, next_node])

    dji(X)
    arr_min_cost = min_costs
    answer = -1
    for i in range(1, N + 1):
        if i == X:
            continue
        min_costs = defaultdict(int)
        i_start_cost = dji(i, X)
        answer = max(answer, arr_min_cost[i] + i_start_cost - 2)

    return answer


print(solution())
