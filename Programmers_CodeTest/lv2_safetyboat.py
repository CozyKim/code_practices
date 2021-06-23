# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

from collections import deque


def solution(people: list, limit: int):
    answer = 0
    people.sort()
    _people = {}

    for idx, p in enumerate(people):
        if p not in _people:
            _people[p] = 1
        else:
            _people[p] += 1          # p 몸무게를 가진 사람수

    # _people = list(set(people)).sort()
    people_deq = deque(people)
    while people_deq:
        n = people_deq.pop()
        if people_deq:
            if people_deq[0] <= limit - n:
                people_deq.popleft()
        answer += 1

    print(answer)
    return answer


solution([70]		, 70)
