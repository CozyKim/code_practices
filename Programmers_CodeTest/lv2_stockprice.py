# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3#
from collections import deque


def solution(prices):
    answer = []

    _price = deque(prices)
    # tmp = [_price.popleft()]
    while _price:
        n = _price.popleft()
        cnt = 0
        flag = 0
        for i in _price:
            if i >= n:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    return answer


solution([1, 2, 3, 2, 3])
