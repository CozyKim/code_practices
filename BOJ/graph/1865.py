# https://www.acmicpc.net/problem/1865

from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

TC = int(input())


def solution():
    edges = []
    N, M, W = map(int, input().split())
    for __ in range(M):
        S, E, T = map(int, input().split())
        edges.append([S, E, T])
        edges.append([E, S, T])
    for __ in range(W):
        S, E, T = map(int, input().split())
        edges.append([S, E, -T])

    INF = 10001 * (W + M)

    def bell_f(start_node):
        distance = [INF] * (N + 1)
        distance[start_node] = 0
        for i in range(N - 1):
            for j in range(2 * M + W):
                cur_node, next_node, cost = edges[j]
                if distance[next_node] > distance[cur_node] + cost:
                    distance[next_node] = distance[cur_node] + cost
        for j in range(2 * M + W):
            cur_node, next_node, cost = edges[j]
            if distance[next_node] > distance[cur_node] + cost:
                distance[next_node] = distance[cur_node] + cost
                return True
        return False

    if bell_f(1):
        return "YES"
    return "NO"


for _ in range(TC):
    print(solution())
