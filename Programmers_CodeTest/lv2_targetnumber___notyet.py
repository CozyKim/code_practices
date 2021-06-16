# https://programmers.co.kr/learn/courses/30/lessons/43165

# 완전 탐색으로 풀이

from collections import deque
from itertools import product


def solution(numbers, target):
    nums = [(-x, x) for x in numbers]
    results = list(map(sum, product(*nums)))
    return results.count(target)


solution([1, 3, 1, 2, 1], 3)

# dfs 풀이
answer = 0


def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if (idx == N and target == value):
        answer += 1
        return
    if idx == N:
        return

    DFS(idx+1, numbers, target, value + numbers[idx])
    DFS(idx+1, numbers, target, value - numbers[idx])


def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer


# bfs 풀이


def solution(numbers, target):
    answer = 0
    stack = deque([(0, 0)])
    while stack:
        currrent_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if currrent_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append([(currrent_sum + number, num_idx + 1)])
            stack.append([(currrent_sum - number, num_idx + 1)])
    return answer
