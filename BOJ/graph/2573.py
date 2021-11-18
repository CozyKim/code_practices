# https://www.acmicpc.net/problem/2573
"""
한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 
최초의 시간(년)을 구하는 프로그램을 작성하시오. 
만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 
프로그램은 0을 출력한다.
"""
import time
import sys
from collections import defaultdict, deque


input = sys.stdin.readline


def main():

    N, M = map(int, input().split())
    tile = []
    start = None
    for i in range(N):
        tile.append(list(map(int, input().split())))
        if start == None:
            for j in range(M):
                if tile[i][j] > 0:
                    start = (i, j)
                    break
    # s_time = time.time()
    CNT = 0

    def num_iceberg(tile):
        cnt = 0
        for line in tile:
            cnt += line.count(0)
        return N * M - cnt

    def bfs(a, b):
        next_tile = {}
        q = deque([(a, b)])
        visited = [[0 for _ in range(M)] for _ in range(N)]
        end = (a, b)
        visit_cnt = 0
        while q:
            cnt = 0
            x, y = q.popleft()
            if visited[x][y] == 1:
                continue
            visited[x][y] = 1
            visit_cnt += 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if tile[x + dx][y + dy] == 0:
                    cnt += 1
                elif tile[x + dx][y + dy] > 0 and visited[x + dx][y + dy] == 0:
                    q.append((x + dx, y + dy))

            next_tile[(x, y)] = max(tile[x][y] - cnt, 0)
            if next_tile[(x, y)] != 0:
                end = (x, y)
        for k, v in next_tile.items():
            tile[k[0]][k[1]] = v
        return end, visit_cnt

    num_ice = num_iceberg(tile)
    end, check = bfs(*start)
    while num_ice == check:
        CNT += 1
        num_ice = num_iceberg(tile)
        end, check = bfs(*end)
        if num_ice == 0:
            return 0

    # print(time.time() - s_time)
    return CNT


print(main())
