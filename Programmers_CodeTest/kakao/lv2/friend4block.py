# https://programmers.co.kr/learn/courses/30/lessons/17679


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    delete_block = set()

    def del_block(r, c):
        nonlocal answer
        if r != m - 1 and c != n - 1:
            if board[r][c] == board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1]:
                delete_block.add((r, c))
                delete_block.add((r + 1, c))
                delete_block.add((r, c + 1))
                delete_block.add((r + 1, c + 1))
                return

    def update(del_blocks):
        for r, c in del_blocks:
            board[r][c] = 0
        r, c = m - 1, 0

        while c < n:
            if not board[r][c]:
                for height in range(r, -1, -1):
                    if board[height][c]:
                        board[r][c], board[height][c] = board[height][c], board[r][c]
                        r -= 1
                r, c = m - 1, c + 1
            else:
                r -= 1
            if r < 0:
                r += m
                c += 1

    for i in range(m):
        for j in range(n):
            del_block(i, j)
    while delete_block:
        answer += len(delete_block)
        update(delete_block)
        delete_block = set()
        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    del_block(i, j)
    print(answer)
    return answer


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
