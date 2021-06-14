from itertools import combinations as com
from functools import reduce


def solution(clothes):
    answer = 0
    have_clothes = {}
    for name, kind in clothes:
        if kind not in have_clothes:
            have_clothes[kind] = 1
        else:
            have_clothes[kind] += 1
    valuelist = list(have_clothes.values())
    valuelist[0] += 1
    return (reduce(lambda x, y: x*(y+1), valuelist) - 1)


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"],
         ["green_turban", "headgear"], ["crowmask", "face"]])
