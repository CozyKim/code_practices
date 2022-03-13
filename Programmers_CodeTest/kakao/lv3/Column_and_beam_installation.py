# https://programmers.co.kr/learn/courses/30/lessons/60061


def solution(n, build_frame):
    answer = []
    # 기둥 조건 평가
    table = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]  # 앞 기둥, 뒤 보

    def check(is_beam, point):
        # 기둥
        if not is_beam:
            if point[0] == 0:
                return True
            if 0 <= point[1] - 1 <= n and table[point[0]][point[1] - 1][1]:
                return True
            if 0 <= point[1] <= n and table[point[0]][point[1]][1]:
                return True
            if 0 <= point[0] - 1 <= n and table[point[0] - 1][point[1]][0]:
                return True
            return False

        # 보
        else:
            if 0 <= point[0] - 1 <= n:
                if table[point[0] - 1][point[1]][0]:
                    return True
                if point[1] + 1 <= n and table[point[0] - 1][point[1] + 1][0]:
                    return True
            if (
                0 <= point[1] + 1 <= n
                and 0 <= point[1] - 1 <= n
                and table[point[0]][point[1] + 1][1]
                and table[point[0]][point[1] - 1][1]
            ):
                return True
            return False

    def building(x, y, a, b):
        if b:
            if check(a, (x, y)):
                table[x][y][a] = 1
        else:
            table[x][y][a] = 0
            if a:  # 보
                check_points = [(0, 0), (-1, 0), (0, 1), (0, -1), (-1, 1)]
            else:  # 기둥
                check_points = [(0, 0), (1, 0), (-1, 0), (1, -1), (0, -1)]
            for dx, dy in check_points:
                if 0 <= x + dx <= n and 0 <= y + dy <= n:
                    for beam, exist in enumerate(table[x + dx][dy + y]):
                        if exist and not check(beam, (dx + x, dy + y)):
                            table[x][y][a] = 1
                            return

    for y, x, a, b in build_frame:
        building(x, y, a, b)
    # print(table)
    for i in range(n + 1):
        for j in range(n + 1):
            if table[i][j][0]:
                answer.append([j, i, 0])
            if table[i][j][1]:
                answer.append([j, i, 1])

    print(sorted(answer, key=lambda x: (x[0], x[1], x[2])))
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))
