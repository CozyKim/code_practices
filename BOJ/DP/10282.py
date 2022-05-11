# https://www.acmicpc.net/problem/10282

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

T = int(input())


def bfs(start):
    global dp, visited
    q = deque([(start, 0)])
    cnt = 1
    while q:
        node, time = q.popleft()

        if not visited[node]:
            cnt += 1
            visited[node] = 1

        for next_node, cost in graph[node]:
            if dp[next_node] > time + cost:
                dp[next_node] = time + cost
                q.append((next_node, time + cost))

    return cnt, max([i for i in dp if i != float("inf")])


for _ in range(T):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    dp = [float("inf")] * (n + 1)
    dp[c] = 0
    visited = [0] * (n + 1)
    visited[c] = 1
    result, max_time = bfs(c)
    print(f"{result} {max_time}")
