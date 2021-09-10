import sys
from itertools import product
from unittest import result
input = sys.stdin.readline


def operation(op):
    tmp = ['1']
    tmp2 = ['1']
    tmp3 = []
    for i, o in enumerate(op):
        if o != ' ':
            tmp.append(o)
            tmp3.append(o)
        tmp2.append(o)
        tmp.append(str(i+2))
        tmp2.append(str(i+2))
    tmp2 = ''.join(tmp2)
    result = ''.join(tmp)
    tmp = result.replace('+', ' ')
    tmp = tmp.replace('-', ' ')
    result2 = list(map(int, tmp.split()))
    sum = result2[0]
    for idx, o in enumerate(tmp3):
        if o == '+':
            sum += int(result2[idx+1])
        elif o == '-':
            sum -= int(result2[idx+1])
    return sum, tmp2


N = int(input())
for _ in range(N):
    num = int(input())
    ops = list(product('+- ', repeat=num-1))
    result = []
    for op in ops:
        n, line = operation(op)
        if n == 0:
            result.append(line)
    for line in sorted(result):
        print(line)
    print()


k = operation(['+', '+', ' '])
