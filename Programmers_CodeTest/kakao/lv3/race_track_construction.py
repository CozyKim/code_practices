# https://programmers.co.kr/learn/courses/30/lessons/67259


from collections import defaultdict


def solution(board):
    min_cost = float("inf")
    mapping = {(1, 0): "d", (-1, 0): "u", (0, 1): "r", (0, -1): "l"}

    def init_list():
        return [[float("inf") for _ in range(len(board))] for _ in range(len(board))]

    cost_table = defaultdict(init_list)
    visited = [[0 for _ in range(len(board))] for _ in range(len(board))]

    def dfs(pos, prev, cost, cnt):
        nonlocal min_cost, visited
        if cost_table[cnt][pos[0]][pos[1]] >= cost:
            cost_table[cnt][pos[0]][pos[1]] = cost
        else:
            return
        if cost >= min_cost:
            return

        if pos == (len(board) - 1, len(board) - 1):
            min_cost = min(min_cost, cost_table[cnt][len(board) - 1][len(board) - 1])
            return

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = pos[0] + dx, pos[1] + dy
            if 0 <= x < len(board) and 0 <= y < len(board):
                if not board[x][y] and not visited[x][y]:
                    visited[x][y] = 1
                    if mapping[(dx, dy)] == prev or prev == None:
                        dfs((x, y), mapping[(dx, dy)], cost + 100, cnt + 1)
                    else:
                        dfs((x, y), mapping[(dx, dy)], cost + 600, cnt + 1)
                    visited[x][y] = 0

    dfs((0, 0), None, 0, 0)

    print(min_cost)
    return min_cost


solution(
    [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
    ]
)
solution(
    [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0],
    ]
)
solution(
    [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0],
    ]
)
inf = 0
tmp1 = [
    [0, 100, 200, 300, 400, 500, 600, inf],
    [100, 700, 800, 900, 1000, 1100, 1200, 1300],
    [200, 800, 900, 1000, 1100, inf, 1800, 1900],
    [300, 900, 1000, 1100, inf, 2500, 1900, 2000],
    [400, 1000, 1100, inf, 2700, 2600, 2000, inf],
    [500, 1100, inf, 3900, 3300, 3200, inf, 5000],
    [600, inf, 4100, 4000, 3400, inf, 4800, 4900],
    [inf, 4300, 4200, 4100, 3500, 4100, 4200, 4300],
]
tmp2 = [
    [0, 100, 200, 300, 400, 500, 600, inf],
    [100, 700, 800, 900, 1000, 1100, 1200, 1300],
    [200, 800, 900, 1000, 1100, inf, 1300, 1900],
    [300, 900, 1000, 1100, inf, 2000, 1400, 2000],
    [400, 1000, 1100, inf, 2200, 2100, 1500, inf],
    [500, 1100, inf, 3400, 2800, 2700, inf, 4500],
    [600, inf, 3600, 3500, 2900, inf, 4300, 4400],
    [inf, 3800, 3700, 3600, 3000, 3600, 3700, 3800],
]
tmp3 = [
    [0, 100, 200, 300, 400],
    [100, inf, inf, inf, 1000],
    [200, 800, inf, 1700, 1100],
    [inf, 1400, 2000, 2100, inf],
    [inf, inf, inf, 2700, 3300],
]
tmptmp = [
    [0, 100, 200, 300, 400],
    [100, inf, inf, inf, 1000],
    [200, 800, inf, 1700, 1100],
    [inf, 1400, 2000, 2100, inf],
    [inf, inf, inf, 2700, 3300],
]
