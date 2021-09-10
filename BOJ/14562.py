import sys
from collections import deque
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    S, T = map(int, input().strip().split())
    q = deque([(S, T, 0)])
    result = 0
    while q:
        s, t, cnt = q.popleft()
        if s == t:
            result = cnt
            break
        q.append((s+1, t, cnt+1))
        if 2*s <= t+3:
            q.append((2*s, t+3, cnt+1))
    print(result)
