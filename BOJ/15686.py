# https://www.acmicpc.net/problem/15686

from collections import defaultdict
import sys

from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

MAP = []
chicken_house = []
houses = []
for r in range(N):
    line = list(map(int, input().split()))
    for c in range(len(line)):
        if line[c] == 2:
            chicken_house.append((r, c))
        if line[c] == 1:
            houses.append((r, c))
    MAP.append(line)


answer = float("inf")

for candi_idx in combinations(chicken_house, M):
    tmp = 0
    houses_dict = defaultdict(lambda: float("inf"))
    for c_r, c_c in candi_idx:
        for r, c in houses:
            houses_dict[(r, c)] = min(abs(c_r - r) + abs(c_c - c), houses_dict[(r, c)])
    for k, v in houses_dict.items():
        tmp += v
    answer = min(answer, tmp)

print(answer)
