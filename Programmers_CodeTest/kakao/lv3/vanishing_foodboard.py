"""
    게임 종료 조건
        1. 움직일 차례인데 캐릭터의 상하좌우 주변 4칸이 모두 발판이 없거나 보드 밖이라서 이동할 수 없는 경우, 해당 차례 플레이어는 패배합니다.
        2. 두 캐릭터가 같은 발판 위에 있을 때, 상대 플레이어의 캐릭터가 다른 발판으로 이동하여 자신의 캐릭터가 서있던 발판이 사라지게 되면 패배합니다.
"""


def solution(board, aloc, bloc):
    answer = -1

    def move(a_r, a_c, b_r, b_c, board, cnt, player):
        if player == 1:
            r, c = a_r, a_c
        else:
            r, c = b_r, b_c

        win = False
        win_cnt = float("inf")
        fall_cnt = cnt
        if board[r][c]:
            board[r][c] = 0

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (
                    0 <= r + dx < len(board)
                    and 0 <= c + dy < len(board[0])
                    and board[r + dx][c + dy]
                ):
                    nr, nc = r + dx, c + dy
                    if player == 1:
                        a_r, a_c = nr, nc
                    else:
                        b_r, b_c = nr, nc
                    n_win, n_cnt = move(a_r, a_c, b_r, b_c, board, cnt + 1, player * -1)
                    if not n_win:
                        win = True
                        win_cnt = min(win_cnt, n_cnt)
                    else:
                        fall_cnt = max(fall_cnt, n_cnt)
            board[r][c] = 1

        return (True, win_cnt) if win else (False, fall_cnt)

    _, answer = move(aloc[0], aloc[1], bloc[0], bloc[1], board, 0, 1)

    return answer
