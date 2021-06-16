# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
from collections import deque


def solution(n, computers):
    answer = 0
    _graph = {}
    for idx, com in enumerate(computers):
        for i in range(0, len(com)):
            if i == idx:
                continue
            if com[i]:
                if idx not in _graph:
                    _graph[idx] = [i]
                else:
                    _graph[idx] += [i]
    # print(_graph)

    answer = BFS(_graph, 0, answer, range(n))
    # print(answer)
    return answer


def BFS(graph, root, answer, left_list):
    queue = deque([root])
    visited = []
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                queue += graph[n]
    answer += 1
    left_list = list(set(left_list) - set(visited))
    if len(left_list) == 0:
        return answer
    answer = BFS(graph, left_list[0], answer, left_list)
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
