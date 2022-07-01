# https://programmers.co.kr/learn/courses/30/lessons/84021


from random import randint

from collections import defaultdict


def solution(game_board, table):
    answer = 0
    dir_map = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visited = [[0] * len(game_board) for _ in range(len(game_board))]
    tmp = []

    def sub_table(r, c, dir, node, prev):
        nonlocal visited, n_node
        visited[r][c] = 1
        for n_dir in range(4):
            dr, dc = dir_map[n_dir]
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(game_board) and 0 <= nc < len(game_board):
                if not visited[nr][nc] and table[nr][nc]:
                    n_node += 1
                    sub_table(nr, nc, n_dir, n_node, node)
        tmp.append((dir, node, prev))
        return node

    blocks = defaultdict(list)
    for r in range(len(game_board)):
        for c in range(len(game_board)):
            if table[r][c] and not visited[r][c]:
                tmp = []
                n_node = 0
                sub_table(r, c, -1, 0, -1)
                block = [0] * len(tmp)
                for dir, node, prev in tmp:
                    block[node] = (dir, node, prev)
                print(block)
                # print(tmp)
                blocks[len(block)].append(block)

    visited = [[0] * len(game_board) for _ in range(len(game_board))]

    def piece_length(r, c):
        cnt = 1
        visited[r][c] = 1
        for n_dir in range(4):
            dr, dc = dir_map[n_dir]
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(game_board) and 0 <= nc < len(game_board):
                if not visited[nr][nc] and not game_board[nr][nc]:
                    cnt += piece_length(nr, nc)
        return cnt

    def checking(r, c):
        for idx, block in enumerate(blocks[piece_length(r, c)]):
            if not len(block):
                return False, None, None
            for dir_bias in range(4):
                block_nodes = [0] * len(block)
                block_nodes[0] = (r, c)
                for dir, node, prev in block:
                    if dir == -1:
                        continue
                    r, c = block_nodes[prev]
                    dir = (dir + dir_bias) % 4
                    dr, dc = dir_map[dir]
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < len(game_board)
                        and 0 <= nc < len(game_board)
                        and not game_board[nr][nc]
                    ):
                        block_nodes[node] = (nr, nc)
                    else:
                        break
                else:
                    return True, len(block), idx
        return False, None, None

    for r in range(len(game_board)):
        for c in range(len(game_board)):
            if not game_board[r][c] and not visited[r][c]:
                is_true, block_leng, idx = checking(r, c)
                if is_true:
                    answer += block_leng
                    blocks[block_leng].pop(idx)
    print(answer)
    return answer


solution(
    [
        [1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0],
    ],
    [
        [1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1],
    ],
)

# solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]])
# N = 30
# solution(
#     [[randint(0, 1) for _ in range(N)] for _ in range(N)],
#     [[randint(0, 1) for _ in range(N)] for _ in range(N)],
# )
