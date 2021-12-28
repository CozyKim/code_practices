# https://www.acmicpc.net/problem/2606

"""
문제 설명
한 컴퓨터가 바이러스에 걸리게 되면 네트워크에 연결되어있는 모든 컴퓨터가 바이러스에 걸리게 된다.
1번 컴퓨터가 바이러스에 걸렸을 때 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수?
"""
import sys
from collections import defaultdict, deque


def main():
    input = sys.stdin.readline

    # 첫째 줄에 컴퓨터의 수가 주어진다. 1~100
    num_com = int(input())
    visited = [0 for _ in range(num_com + 1)]
    visited[1] = 1
    # 둘째 줄에는 네트워크 상에서 직접 열결되어있는 컴퓨터 쌍의 수가 주어진다.
    pair_com = int(input())
    graph = defaultdict(list)
    # 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

    # 그래프를 만들어 주는 함수
    def mapping(a, b):
        graph[a].append(b)
        graph[b].append(a)

    for _ in range(pair_com):
        a, b = map(int, input().strip().split())
        mapping(a, b)

    def bfs():
        q = deque()
        q.append(1)
        while q:
            pos = q.popleft()
            # if visited[pos]:
            #     continue
            for i in graph[pos]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
        return sum(visited) - 1

    return bfs()


print(main())
