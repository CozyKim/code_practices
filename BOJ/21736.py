import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
campus = []
blocks = []
pos = None
for i in range(N):
    line = input().strip()
    if pos == None:
        if 'I' in line:
            j = line.index('I')
            pos = (i, j)
    campus.append(line)

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
stack = [pos]
cnt = 0
visited = [pos]
while stack:
    x, y = stack.pop()
    for dx, dy in dir:
        if (x + dx, y + dy) not in visited and 0 <= x + dx < N and 0 <= y + dy < M and campus[x+dx][y+dy] != 'X':
            if campus[x+dx][y+dy] == 'P':
                cnt += 1
            stack.append((x + dx, y + dy))
            visited.append((x + dx, y + dy))
if cnt:
    print(cnt)
else:
    print('TT')
