import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
global tiles
tiles = []
for _ in range(N):
    tiles.append(list(map(int, input().strip().split())))

q = deque()
q.append((0, 0))
result = False
while q:
    pos = q.popleft()
    steps = tiles[pos[0]][pos[1]]
    if steps == -1:
        result = True
        break
    elif steps == 0:
        continue
    if pos[0]+steps < N:
        q.append((pos[0] + steps, pos[1]))
    if pos[1]+steps < N:
        q.append((pos[0], pos[1] + steps))

if result:
    print('HaruHaru')
else:
    print('Hing')
