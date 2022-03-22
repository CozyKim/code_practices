# https: // programmers.co.kr/learn/courses/30/lessons/42884?language = python3
from collections import deque


def solution(routes):
    answer = 0
    q = deque(sorted(routes, key=lambda x: x[1]))
    while q:
        s, e = q[0]
        while q:
            s, ne = q.popleft()
            if s > e:
                q.appendleft([s, ne])
                break
        # if q:
        answer += 1
    return answer
