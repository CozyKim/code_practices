# https://www.acmicpc.net/problem/1629


A, B, C = map(int, input().split())


def d_n_c(a, b):
    if b == 1:
        return a % C

    tmp = d_n_c(a, b // 2)

    if b % 2 == 0:
        return tmp * tmp % C

    else:
        return tmp * tmp * a % C


print(d_n_c(A, B))
