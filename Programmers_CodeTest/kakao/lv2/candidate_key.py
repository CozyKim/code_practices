# https://programmers.co.kr/learn/courses/30/lessons/42890


from collections import defaultdict, deque
import itertools

# 풀이1 : 조합으로 풀기 -> 실패
# def solution(relation):
#     answer = 0

#     def check(column: tuple):
#         check_dict = defaultdict(int)
#         for re in relation:
#             tmp = []
#             for atrr in column:
#                 tmp.append(re[atrr])
#             if check_dict[tuple(tmp)]:
#                 return False
#             check_dict[tuple(tmp)] = 1
#         return True

#     attributes = [i for i in range(len(relation[0]))]
#     max_i = len(attributes)
#     i = 1
#     passed = []
#     while max_i + 1 > i:
#         new_passed = []
#         for k in list(itertools.combinations(attributes, i)):
#             pass_trig = False
#             for attr in k:
#                 if attr in passed:
#                     pass_trig = True
#             if pass_trig:
#                 continue
#             if check(k):
#                 for attr in k:
#                     # attributes.pop(attributes.index(attr))
#                     new_passed.append(attr)
#                 answer += 1
#         i += 1
#         passed += new_passed
#     print(answer)
#     return answer

# # 해결해야할 부분 : (1), (2,3), (2,4,5) 마지막 부분이 들어갈 수 있게 고치자
# solution(
#     [
#         ["100", "ryan", "music", "2"],
#         ["200", "apeach", "math", "2"],
#         ["300", "tube", "computer", "3"],
#         ["400", "con", "computer", "4"],
#         ["500", "muzi", "music", "3"],
#         ["600", "apeach", "music", "2"],
#     ]
# )
# dfs 로 풀 수도 있을 듯
def solution(relation):
    answer = 0
    tmp = []
    attributes = [i for i in range(len(relation[0]))]

    def check(column: tuple):
        check_dict = defaultdict(int)
        for re in relation:
            tmp = []
            for atrr in column:
                tmp.append(re[atrr])
            if check_dict[tuple(tmp)]:
                return False
            check_dict[tuple(tmp)] = 1
        return True

    def dfs(column: tuple):
        # 종료 조건
        nonlocal answer
        if check(column):
            tmp.append(column)

        for i in range(list(column)[-1] + 1, len(relation[0])):
            dfs({*list(column), i})

    for i in attributes:
        dfs(tuple([i]))

    keys_length = [[] for _ in range(8)]
    for sub in sorted(tmp, key=len):
        iskey = True
        for leng in keys_length[: len(sub)]:
            for key in leng:
                if len(set(key) - set(sub)) == 0:
                    iskey = False
                    break
        if iskey:
            answer += 1
            keys_length[len(sub) - 1].append(sub)
    print(sorted(tmp, key=len))
    print(keys_length)
    print(answer)
    return answer


solution(
    [
        ["a", 1, "aaa", "c", "ng"],
        ["b", 1, "bbb", "c", "g"],
        ["c", 1, "aaa", "d", "ng"],
        ["d", 2, "bbb", "d", "ng"],
    ]
)
solution(
    [
        ["a", "1", "aaa", "c", "ng"],
        ["a", "1", "bbb", "e", "g"],
        ["c", "1", "aaa", "d", "ng"],
        ["d", "2", "bbb", "d", "ng"],
    ]
)
solution(
    [
        ["a", 1, "aaa", "c", "ng"],
        ["b", 1, "bbb", "c", "g"],
        ["c", 1, "aaa", "d", "ng"],
        ["d", 2, "bbb", "d", "ng"],
    ]
)
solution(
    [
        ["a", 1, "aaa", "c", "ng"],
    ]
)
solution(
    [
        ["a", "1", "aaa", "c", "ng"],
        ["a", "1", "bbb", "e", "g"],
        ["c", "1", "aaa", "d", "ng"],
        ["d", "2", "bbb", "d", "ng"],
    ]
)
