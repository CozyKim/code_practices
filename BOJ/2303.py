import sys
from itertools import combinations


def find_max_card(n: list):
    combi = set(combinations(n, 3))
    dex_max = 0
    for i in combi:
        dex = sum(i) % 10
        if dex_max <= dex:
            dex_max = dex
    return dex_max


input = sys.stdin.readline
N = int(input())
tmp = {}
for idx, _ in enumerate(range(N)):
    n = list(map(int, input().split()))
    card_result = find_max_card(n)
    tmp[card_result] = idx + 1
result = max(tmp.keys())
print(tmp[result])
