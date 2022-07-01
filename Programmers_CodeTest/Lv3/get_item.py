# https://programmers.co.kr/learn/courses/30/lessons/87694


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = float("inf")
    board = [[0] * 102 for _ in range(102)]

    def fill_rec(lx, ly, rx, ry):
        for r in range(ly, ry + 1):
            for c in range(lx, rx + 1):
                if r == ly or r == ry or c == lx or c == rx:
                    if board[r][c] == 0:
                        board[r][c] = 1
                else:
                    board[r][c] = 2

    for lx, ly, rx, ry in rectangle:
        fill_rec(2 * lx, 2 * ly, 2 * rx, 2 * ry)

    def move(r, c, pr, pc, cnt):
        nonlocal answer
        if r == 2 * itemY and c == 2 * itemX:
            answer = min(answer, cnt // 2)
            return

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nr == pr and nc == pc:
                continue
            if 0 <= nr < 102 and 0 <= nc < 102:
                if board[nr][nc] == 1:
                    board[nr][nc] = -1
                    move(nr, nc, r, c, cnt + 1)
                    board[nr][nc] = 1

    board[2 * characterY][2 * characterX] = -1

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = 2 * characterY + dr, 2 * characterX + dc
        if board[nr][nc] == 1:
            board[nr][nc] = -1
            move(nr, nc, 2 * characterY, 2 * characterX, 1)
            board[nr][nc] = 1

    print(answer)
    return answer


solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
