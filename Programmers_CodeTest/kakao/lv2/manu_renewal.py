# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3
"""
문제 설명

단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성
이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품 메뉴들을 코스 요리로 구성하기로 함

코스요리는 최소 2가지 이상의 단품메뉴
최소 2명이상의 손님으로부터 주문된 단품 메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함

문제
input : orders - 각 손님들이 주문한 단품 메뉴들의 문자열(Union[str]) , course - 코스요리를 구성하는 단품 메뉴들의 개수(Union[int])
output : result - 새로 추가하게 될 코스 요리의 메뉴 구성

제한 사항
2<=len(orders)<=20
orders 각 배열의 원소의 크기 2이상 10이하, 대문자로만 이뤄져 있음, 각 문자열에 알파벳 중복 없음
course 오름차순 정렬

result : 오름차순
"""

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 5]
import time

from collections import Counter
from itertools import combinations, chain
import re


def solution(orders, course):
    # start = time.time()
    result = []
    orders = list(map("".join, map(sorted, orders)))
    cnt_dict = [[] for _ in range(len(course))]

    for idx, i in enumerate(course):
        max_cnt = 2
        combis = set()
        for menu in orders:
            combis |= set(combinations(menu, i))
        for x in combis:
            x = sorted(x)
            cnt = 0
            for y in orders:
                if re.search("[A-Z]*".join(x) + "+", y):
                    cnt += 1
            if cnt > 1:
                if max_cnt > cnt:
                    continue
                if max_cnt == cnt:
                    cnt_dict[idx].append("".join(x))
                else:
                    cnt_dict[idx] = ["".join(x)]
                    max_cnt = cnt
    for c in cnt_dict:
        result += c
    # print(time.time() - start)
    return sorted(result)


print(solution(orders, course))
