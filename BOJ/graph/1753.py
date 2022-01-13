# https://www.acmicpc.net/problem/1753
"""
문제
방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램 작성
단, 모든 간선의 가중치는 10 이하의 자연수

input : 
    첫째 줄
        V : 정점의 개수, 모든 정점에는 1~V 까지 번호가 매겨져 있다.
        E : 간선의 개수
    둘째 줄
        K : 정점의 시작번호 (1<= K <= V)
    셋째 줄 부터
        u,v,w : u-> v로 가는 가중치 w / 두 정점 사이에 여러개의 간선이 존재할 수도 있다.
output:
    첫째 줄부터 V개의 줄에 걸쳐, i 번째 줄에 i 번 정점으로의 최단 경로의 경로값을 출력
    경로 존재 안할 경우 INF
"""
import sys
from collections import defaultdict, deque
import heapq

input = sys.stdin.readline


def main():
    # 입력들
    V, E = map(int, input().strip().split())
    K = int(input())

    # 그래프 입력
    graph = defaultdict(list)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])

    # heap을 이용한 다익스트라로 최단 경로 구하기
    D = [[0, K]]
    min_costs = defaultdict(int)
    while D:
        min_cost, node = heapq.heappop(D)
        if not min_costs[node]:
            min_costs[node] = min_cost
        else:
            continue
        for next_node, cost in graph[node]:
            if not min_costs[next_node] and next_node != K:
                heapq.heappush(D, (cost + min_cost, next_node))

    # print(min_costs)
    for i in range(1, V + 1):
        if not min_costs[i]:
            if i == K:
                print(0)
            else:
                print("INF")
        else:
            print(min_costs[i])


if __name__ == "__main__":
    main()
