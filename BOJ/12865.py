# https://www.acmicpc.net/problem/12865

import sys


def backpack(wv, k):
    mem = [None]*(len(wv)+1)
    for i in range(len(wv)+1):
        mem[i] = [None]*(k+1)
    for i in range(len(wv)+1):
        for j in range(k+1):
            if i == 0 or j == 0:
                mem[i][j] = 0
            elif wv[i-1][0] > j:
                mem[i][j] = mem[i-1][j]
            else:
                mem[i][j] = max(mem[i-1][j], mem[i-1][j-wv[i-1][0]]+wv[i-1][1])
    return mem[len(wv)][k]


N, K = map(int, sys.stdin.readline().split())
WV = [None] * N
for i in range(N):
    WV[i] = list(map(int, sys.stdin.readline().split()))
print(backpack(WV, K))
