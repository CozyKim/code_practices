import sys
A = []


def Coin0(a: list, k: int):
    cnt = 0
    for i in range(len(a)-1, -1, -1):
        if k >= a[i]:
            cnt += k//a[i]
            k -= a[i] * (k//a[i])
    return cnt


N, K = map(int, sys.stdin.readline().split())
for _ in range(N):
    A.append(int(sys.stdin.readline()))
print(Coin0(A, K))
