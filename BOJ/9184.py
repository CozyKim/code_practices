# https://www.acmicpc.net/problem/9184

import sys
input = sys.stdin.readline
w_abc = {}
while 1:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break

    def w(a, b, c):
        if (a, b, c) in w_abc:
            return w_abc[(a, b, c)]
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)
        if a < b and b < c:
            w_abc[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return w_abc[(a, b, c)]
        else:
            w_abc[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + \
                w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return w_abc[(a, b, c)]
    print(f'w({a}, {b}, {c}) = '+str(w(a, b, c)))
