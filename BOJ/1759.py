# https://www.acmicpc.net/problem/1759
from itertools import combinations


L, C = map(int, input().split())
chars = list(input().split())
chars.sort()
exception_list = list(map(''.join, list(combinations(chars, L))))
exception_list.sort()
for cha in exception_list:
    cnt_vow = 0
    for c in cha:
        if c in 'aeiou':
            cnt_vow += 1
    if len(cha) - cnt_vow >= 2 and cnt_vow >= 1:
        print(cha)
