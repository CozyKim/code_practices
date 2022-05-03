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
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    menu_cnt = defaultdict(int)
    course_max = defaultdict(int)
    course_list = defaultdict(list)

    for order in orders:
        for i in range(2, len(order) + 1):
            for sets in combinations(sorted(order), i):
                menu_cnt["".join(sets)] += 1

    for k, v in menu_cnt.items():
        if v >= 2:
            if course_max[len(k)] < v:
                course_max[len(k)] = v
                course_list[len(k)] = [k]
            elif course_max[len(k)] == v:
                course_list[len(k)].append(k)

    for i in course:
        answer += course_list[i]

    return sorted(answer)
