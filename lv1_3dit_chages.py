def solution(n):
    return ThreetoTen(TentoThree(n))


def TentoThree(n):
    N = ''
    while n > 0:
        N += str(n % 3)
        n = n//3
    return N


def ThreetoTen(n: str):
    N = 0
    for k, i in enumerate(n):
        N += (3**(len(n)-1-k)) * int(i)
    return N


print(ThreetoTen(TentoThree(125)))
