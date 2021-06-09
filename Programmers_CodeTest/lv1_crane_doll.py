def solution(board, moves):
    answer = 0
    last_doll = [0]
    empty = []
    for m in moves:
        if m in empty:
            continue
        tmp = pick(board, len(board), m)
        if tmp == 0:
            empty.append(m)
        elif last_doll[-1] == tmp:
            answer += 1
            last_doll.pop()
        else:
            last_doll.append(tmp)
    return answer


def pick(board, board_depth: int, choice: int):
    for i in range(board_depth):
        if board[i][choice-1] != 0:
            tmp = board[i][choice-1]
            board[i][choice-1] = 0
            return tmp

    return 0


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
