# https://programmers.co.kr/learn/courses/30/lessons/67258


# 투포인터 활용
from collections import defaultdict


def solution(gems):
    answer = []
    gems_sets = set(gems)
    cnt_gems = defaultdict(int)

    left, right = 0, 0
    min_length = float("inf")
    while right < len(gems) or len(cnt_gems) == len(gems_sets):
        if len(cnt_gems) != len(gems_sets):
            cnt_gems[gems[right]] += 1
            right += 1
        else:
            cnt_gems[gems[left]] -= 1
            if cnt_gems[gems[left]] == 0:
                cnt_gems.pop(gems[left])
                if right - left < min_length:
                    min_length = right - left
                    answer = [left + 1, right]
            left += 1

    return answer


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
