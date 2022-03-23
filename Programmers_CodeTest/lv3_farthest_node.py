# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import defaultdict
import heapq


def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    cnt_dict = defaultdict(int)
    cnt_table = [[1, 1]]  # cnt, node
    while cnt_table:
        cnt, node = heapq.heappop(cnt_table)
        if cnt_dict[node]:
            continue
        cnt_dict[node] = cnt
        for next_node in graph[node]:
            heapq.heappush(cnt_table, [cnt + 1, next_node])

    print(cnt_dict)
    return list(cnt_dict.values()).count(max(cnt_dict.values()))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
