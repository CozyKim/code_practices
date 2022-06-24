# https://programmers.co.kr/learn/courses/30/lessons/86052


def solution(grid):
    answer = []
    visited = [
        [[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))
    ]  # 위입, 좌입, 아입, 우입
    dir_map = {
        0: (-1, 0),
        1: (0, -1),
        2: (1, 0),
        3: (0, 1),
    }  # 상, 좌, 하, 우

    def dfs(dir, r, c, cnt):
        while 1:
            if len(grid) <= r:
                r = 0
            elif r < 0:
                r = len(grid) - 1

            if len(grid[0]) <= c:
                c = 0
            elif c < 0:
                c = len(grid[0]) - 1

            if visited[r][c][dir]:
                answer.append(cnt - 1)
                return
            visited[r][c][dir] = cnt
            if grid[r][c] == "L":
                dir = (dir + 1) % 4
            elif grid[r][c] == "R":
                dir = (dir - 1) if dir > 0 else 3
            r, c = r + dir_map[dir][0], c + dir_map[dir][1]
            cnt += 1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for dir in range(4):
                if not visited[r][c][dir]:
                    dfs(dir, r, c, 1)

    return sorted(answer)


solution(["SL", "LR"])
solution(["S"])
solution(["R", "R"])
