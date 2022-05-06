# https://programmers.co.kr/learn/courses/30/lessons/72415
from collections import deque
from itertools import permutations


def solution(board, r, c):
    answer = float("inf")

    def move_shift(r, c, dr, dc, board):
        r, c, = (
            r + dr,
            c + dc,
        )
        while 0 <= r < 4 and 0 <= c < 4:
            if board[r][c]:
                return r, c
            r, c, = (
                r + dr,
                c + dc,
            )
        return r - dr, c - dc

    def find_card(r, c, card, board):
        visited = [[0] * 4 for _ in range(4)]
        q = deque([(r, c, 0)])
        while q:
            x, y, cnt = q.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = 1
            if board[x][y] == card:
                cnt += 1
                board[x][y] = 0
                return x, y, cnt, board
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                sx, sy = move_shift(x, y, dx, dy, board)
                if not visited[sx][sy]:
                    q.append((sx, sy, cnt + 1))
                if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
                    q.append((nx, ny, cnt + 1))

    all_card = set()
    for cards in list(map(set, board)):
        all_card |= cards
    all_card.discard(0)
    check = [0] * 7
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if not check[board[i][j]]:
                    check[board[i][j]] = 1
                else:
                    board[i][j] *= -1

    def culculate(r, c, idx, order, cnt, board):
        nonlocal answer
        if cnt > answer:
            return
        if idx == len(order):
            answer = min(answer, cnt)
            return
        for card1, card2 in [(1, -1), (-1, 1)]:
            card1, card2 = card1 * order[idx], card2 * order[idx]
            r1, c1, tmp1, board = find_card(r, c, card1, board)
            r2, c2, tmp2, board = find_card(r1, c1, card2, board)
            culculate(r2, c2, idx + 1, order, tmp1 + tmp2 + cnt, board)
            board[r1][c1] = card1
            board[r2][c2] = card2

    for order in list(permutations(all_card, len(all_card))):
        x, y = r, c
        culculate(x, y, 0, order, 0, board)

    return answer
