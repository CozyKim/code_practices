# https://www.acmicpc.net/problem/15685

import sys

input = sys.stdin.readline

direction_map = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}

dragon_curve_gen = [[None] for _ in range(11)]

answer = 0

board_size = 101


def make_curve(gen, prev_dir, max_gen):
    global dragon_curve_gen
    if gen == max_gen + 1:
        return
    if gen > 0:
        new_dir = [(prev_dir[idx] + 1) % 4 for idx in range(len(prev_dir) - 1, -1, -1)]
        dragon_curve_gen[gen] = prev_dir + new_dir
    else:
        dragon_curve_gen[gen] = prev_dir
    make_curve(gen + 1, dragon_curve_gen[gen][:], max_gen)


N = int(input())
board = [[0] * board_size for _ in range(board_size)]
curve_info = []  # c, r, dir, gen
curve_info = [list(map(int, input().split())) for _ in range(N)]

make_curve(0, [0], max(curve_info, key=lambda x: x[3])[3])

for c, r, dir, gen in curve_info:
    board[r][c] = 1
    for dra_dir in dragon_curve_gen[gen]:
        dra_dir = (dra_dir + dir) % 4
        dr, dc = direction_map[dra_dir]
        r, c = r + dr, c + dc
        board[r][c] = 1

for i in range(board_size):
    for j in range(board_size):
        if i == board_size - 1 or j == board_size - 1:
            continue
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            answer += 1
print(answer)
