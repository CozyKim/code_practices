from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
stepping_stones = list(map(int, input().strip().split()))
a, b = map(int, input().strip().split())
result = -1
if a != b:
    start = a-1
    q = deque([(start, 1)])
    visited = []
    while q:
        pos, cnt = q.popleft()
        visited.append(pos)
        for i in range(stepping_stones[pos], N, stepping_stones[pos]):
            if pos + i == b - 1 or pos - i == b - 1:
                result = cnt
                break
            if 0 <= pos + i < N and pos + i not in visited:
                q.append((pos+i, cnt+1))
            if 0 <= pos - i < N and pos - i not in visited:
                q.append((pos-i, cnt+1))

        if result != -1:
            break
else:
    result = 0
print(result)
