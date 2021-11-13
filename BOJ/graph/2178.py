# https://www.acmicpc.net/problem/2178
from collections import deque
import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    tile = []
    for i in range(N):
        tile.append(list(input().strip()))
    tile[0][0] = 1

    def bfs(a, b):
        q = deque([(a, b)])
        while q:
            n, m = q.popleft()
            for dn, dm in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= n + dn < N and 0 <= m + dm < M:
                    if tile[n + dn][m + dm] == "1":
                        tile[n + dn][m + dm] = tile[n][m] + 1
                        q.append((n + dn, m + dm))

    bfs(0, 0)
    print(tile[N - 1][M - 1])


if __name__ == "__main__":
    main()
