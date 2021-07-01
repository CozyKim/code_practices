# https://www.acmicpc.net/problem/5430


import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    tmp = input().rstrip(']\n').lstrip('[').split(',')
    if tmp != '':
        arr = deque(tmp)
    flag = 1
    if n < p.count('D'):
        print('error')
        continue
    if 'RR' in p:
        p.replace('RR', '')
    for op in p:
        if op == 'R':
            flag *= -1
        elif op == 'D' and flag == 1:
            arr.popleft()
        elif op == 'D' and flag == -1:
            arr.pop()
    if flag == 1:
        print('['+','.join(list(arr))+']')
    else:
        print('['+','.join(list(reversed(arr)))+']')
