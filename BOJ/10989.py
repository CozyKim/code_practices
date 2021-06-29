import sys
from collections import OrderedDict
input = sys.stdin.readline

N = int(input())
heap = []
tmp = {}
for _ in range(N):
    n = int(input())
    if n not in tmp:
        tmp[n] = 1
    else:
        tmp[n] += 1
ordered = OrderedDict(sorted(tmp.items(), key=lambda x: x[0]))

for n, i in ordered.items():
    for _ in range(i):
        print(n)
