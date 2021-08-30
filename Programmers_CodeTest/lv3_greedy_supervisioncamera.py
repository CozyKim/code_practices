# https: // programmers.co.kr/learn/courses/30/lessons/42884?language = python3
from collections import deque

# 다시 풀때 routes 그대로 이용하는데 정렬을 시작기준, 끝나는 기준 2개로 나눠서 풀기


def solution(routes):
    answer = 0
    start = []
    end = []
    for s, e in routes:
        start.append(s)
        end.append(e)

    start.sort()
    end.sort()
    end = deque(end)

    while end:
        e = end.popleft()
        cnt = 0
        for s in start:
            if e < s:
                break
            else:
                cnt += 1
        if cnt != 0:
            answer += 1
            start = start[cnt:]

    return answer

# def solution(routes):
#     answer = 0
#     tmp = []
#     for s, e in routes:
#         tmp.append([s, 0])
#         tmp.append([e, 1])

#     tmp.sort()
#     route = deque(tmp)
#     flag = 0
#     while route:
#         position, end = route.popleft()
#         if end and not flag:
#             flag = 1
#             answer += 1
#         if not end:
#             flag = 0

#     return answer


# solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])
# print(solution([[-2, -1], [1, 2], [-3, 0]]))  # 2
# print(solution([[0, 0], ]))  # 1
# print(solution([[0, 1], [0, 1], [1, 2]]))  # 1
# print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))  # 4
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
# print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
