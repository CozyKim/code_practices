# https://programmers.co.kr/learn/courses/30/lessons/42626
def solution(scoville: list, K: int):
    answer = 0
    scoville.sort(reverse=True)
    if scoville[-1] + scoville[-2] == 0:
        answer = -1
    else:
        while len(scoville) > 1:
            min1 = scoville.pop()
            min2 = scoville.pop()
            if min1 >= K:
                return answer
            else:
                scoville.append(make_new_scoville(min1, min2))
                scoville.sort(reverse=True)
                answer += 1
        if scoville[0] >= K:
            return answer
        else:
            return -1


def make_new_scoville(a, b):
    return a + b * 2


print(solution([1, 2, 3, 9, 10, 12], 7))
