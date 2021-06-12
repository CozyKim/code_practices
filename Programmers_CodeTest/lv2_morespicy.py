# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min1 = heapq.heappop(scoville)
    min2 = heapq.heappop(scoville)

    while len(scoville) > 0:
        if min1 >= K:
            return answer
        else:
            min1 = heapq.heappushpop(
                scoville, make_new_scoville(min1, min2))
            if len(scoville) > 0:
                min2 = heapq.heappop(scoville)
            answer += 1
    if min1 >= K:
        return answer
    elif make_new_scoville(min1, min2) >= K:
        return answer + 1
    else:
        return -1


def make_new_scoville(a, b):
    return a + b * 2


print(solution([1, 2, 3], 6))
