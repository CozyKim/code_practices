import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
campus = []
blocks = []
pos = None
for i in range(N):
    line = input().strip()
    if pos == None:
        if "I" in line:
            j = line.index("I")
            pos = (i, j)
    campus.append(line)

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
stack = [pos]
cnt = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[pos[0]][pos[1]] = 1
flag = 0
while stack:
    x, y = stack.pop()
    for dx, dy in dir:
        if 0 <= x + dx < N and 0 <= y + dy < M:
            if not visited[x + dx][y + dy] and campus[x + dx][y + dy] != "X":
                if campus[x + dx][y + dy] == "P":
                    cnt += 1
                stack.append((x + dx, y + dy))
                visited[x + dx][y + dy] = 1
    if flag:
        break
if cnt:
    print(cnt)
else:
    print("TT")
