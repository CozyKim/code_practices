# https://www.acmicpc.net/problem/11657

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

INF = 10001 * 6000


def solution():
    def bell_f():
        distance = [INF] * (N + 1)
        distance[1] = 0
        for _ in range(N - 1):
            for s, e, cost in edges:
                # distance[s]가 INF 가 아님을 확인함으로써 출발 지점(노드1)으로 부터 이어진 그래프인지 판별
                if distance[s] != INF:
                    distance[e] = min(distance[e], distance[s] + cost)
        for s, e, cost in edges:
            if distance[s] != INF:
                if distance[e] > distance[s] + cost:
                    return -1
        return distance

    answer = bell_f()
    if answer == -1:
        print(-1)
        return
    for i in range(2, N + 1):
        if answer[i] == INF:
            print(-1)
        else:
            print(answer[i])


solution()
