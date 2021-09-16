from copy import deepcopy
import sys


def flopping(line, N, idxs):
    line_copy = deepcopy(line)
    Index = []
    dir = [-1, 0, 1]
    for idx, tile in enumerate(line_copy):
        if tile == '#':
            Index.append(idx)
    if idxs != None:
        for idx in idxs:
            line_copy[idx] = ('#' if line_copy[idx] == '.' else '.')
    for idx in Index:
        for col in dir:
            if 0 <= idx + col < N:
                if line_copy[idx + col] == '.':
                    line_copy[idx + col] = '#'
                elif line_copy[idx + col] == '#':
                    line_copy[idx + col] = '.'

    return line_copy, Index


input = sys.stdin.readline
N = int(input())
lines = [[]*N for _ in range(N)]
lines[0] = list(input().rstrip())
next_flop_idxs = None
for i in range(1, N):
    lines[i], next_flop_idxs = flopping(lines[i-1], N, next_flop_idxs)

for line in lines:
    print(''.join(line))


"""

10010
01101
01110
10110
01001

01101
11111
01110  00011  10110
10110
01001
"""
