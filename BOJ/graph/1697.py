# https://www.acmicpc.net/problem/1697
"""
문제 설명
숨바꼭질 중이다.
수빈이는 점 N에 있고 동생은 점 K에 있다. 
수빈이는 걷거나 순간이동 가능
수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1 로 이동하게 된다
순간이동을 하는 경우 1초 후 2*X의 위치로 이동
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인가?
"""
from collections import deque

# 수빈이의 위치 N, 동생의 위치 K
N, K = map(int, input().split())

# 이미 지나간 곳
visited = [0 for _ in range(min(2 * max(N, K) + 1, 150001))]
visited[N] = 1


def bfs():
    q = deque()
    CNT = 0
    q.append((N, CNT))
    if N == K:
        return 0
    while q:
        pos, cnt = q.popleft()

        nexts = [pos + 1, pos - 1, pos * 2]

        if K in nexts:
            return cnt + 1

        # 다음 위치가 visited 범위를 넘어서선 안된다.
        for n in nexts:
            if 0 <= n <= len(visited) - 1:
                if not visited[n]:
                    visited[n] = 1
                    q.append((n, cnt + 1))


print(bfs())
