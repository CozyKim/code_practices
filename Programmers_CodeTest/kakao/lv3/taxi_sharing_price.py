# https://programmers.co.kr/learn/courses/30/lessons/72413
"""
문제 : A와 B가 합승하여 요금이 최저인 경로로 갔을 때 비용은?
    n : 지점의 개수
    s : 출발 지점
    a : A의 도착지점
    b : B의 도착지점
    fares : 지점사이의 택시요금 나타냄

    만약, 아예 합승하지 않고 각자 이동하는 경우 예상 요금이 쌀 때 합승하지 않아도 된다.
"""
from collections import defaultdict
import heapq


def solution(n, s, a, b, fares):
    answer = float("inf")
    graph = defaultdict(list)
    for x, y, cost in fares:
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    def dji(start, end):
        costs = defaultdict(int)
        h = [(0, start)]
        while h:
            cost, node = heapq.heappop(h)
            if node == end:
                return cost
            if node in costs:
                continue
            costs[node] = cost
            for next_node, next_cost in graph[node]:
                heapq.heappush(h, (cost + next_cost, next_node))
        return float("inf")

    for i in range(1, n + 1):
        answer = min(answer, dji(s, i) + dji(i, a) + dji(i, b))
    return answer
