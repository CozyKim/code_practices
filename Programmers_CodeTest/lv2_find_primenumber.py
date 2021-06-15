# def solution(numbers):
#     answer = 0
#     count = {}
#     for n in numbers:
#         if int(n) not in count:
#             count[int(n)] = 1
#         else:
#             count[int(n)] += 1
#     count_sorted = sorted(list(count.keys()), reverse=True)
#     maximum = ''
#     for i in count_sorted:
#         maximum += str(i) * count[i]
#     # print(maximum)

#     maximum = int(maximum)
#     primetable = [True] * (maximum + 1)
#     for i in range(2, maximum+1):
#         if not primetable[i]:
#             continue
#         for j in range(2*i, maximum+1, i):
#             primetable[j] = False
#     # print(primetable)

#     primenums = []
#     for idx, _bool in enumerate(primetable):
#         if idx != 0 and idx != 1:
#             if _bool:
#                 primenums.append(idx)
#     # print(primenums)
#     primenums = list(map(str, primenums))
#     # print(primenums)

#     for n in primenums:
#         cnt = 0
#         for nn in n:
#             if int(nn) in count:
#                 if n.count(nn) <= count[int(nn)]:
#                     cnt += 1
#         if cnt == len(n):
#             answer += 1

#     print(answer)
#     return answer
from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


print(solution("0"))
