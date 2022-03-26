# https://www.acmicpc.net/problem/1967

from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    graph[parent].append([child, weight])

diameter = 0


def parents_max_weight(node):
    global diameter
    if node not in graph:
        return 0
    first = 0
    second = 0
    for child, cost in graph[node]:
        check = parents_max_weight(child) + cost
        if check > first:
            first, second = check, first
        else:
            if check > second:
                second = check
    diameter = max(diameter, first + second)
    return first


parents_max_weight(1)
print(diameter)
