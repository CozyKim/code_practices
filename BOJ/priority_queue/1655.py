# https://www.acmicpc.net/problem/1655

import heapq, sys

input = sys.stdin.readline

N = int(input())

left = []
right = []
center = None
for i in range(N):
    n = int(input())
    if i == 0:
        center = n
        print(center)
        continue
    if center <= n:
        heapq.heappush(right, n)
    else:
        heapq.heappush(left, -n)

    if len(right) > len(left) + 1:
        heapq.heappush(left, -center)
        center = heapq.heappop(right)
    elif len(right) < len(left):
        heapq.heappush(right, center)
        center = -heapq.heappop(left)
    print(center)
