# https://www.acmicpc.net/problem/6603

from itertools import combinations
import sys
input = sys.stdin.readline
S = [1]
while 1:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    _S = S[1:]
    _S = sorted(list(combinations(_S, 6)))
    for s in _S:
        print(*s)
    print()
