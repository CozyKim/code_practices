# https://programmers.co.kr/learn/courses/30/lessons/72413
"""
문제 : A와 B가 합승하여 요금이 최저인 경로로 갔을 때 비용은?
    n : 지점의 개수
    s : 출발 지점
    a : A의 도착지점
    b : B의 도착지점
    fares : 지점사이의 택시요금 나타냄

    만약, 아예 합승하지 않고 각자 이동하는 경우 예상 요금이 쌀 때 합승하지 않아도 된다.
"""
from cmath import inf
from collections import defaultdict
import heapq
import time

n = 6
s = 4
a = 5
b = 6
fares = [
    [2, 6, 6],
    [6, 3, 7],
    [4, 6, 7],
    [6, 5, 11],
    [2, 5, 12],
    [5, 3, 20],
    [2, 4, 8],
    [4, 3, 9],
]


def solution(n, s, a, b, fares):
    answer = 0
    graph = defaultdict(dict)

    # 그래프 그려주는 함수
    def set_graph(a, b, cost):
        graph[a][b] = cost
        graph[b][a] = cost

    for n1, n2, cost in fares:
        set_graph(n1, n2, cost)
    print(graph.items())
    return answer


# solution(n, s, a, b, fares)
""" 
풀이 1
1. S에서 A, B 각자의 목적지 까지 가는데 경로와 비용 저장
2. 그 경로에서 앞에서 부터 겹친 만큼 비용 계산 => 전체 경비 = 해당 A경비 + 해당 B경비 - 겹친 만큼 비용
"""

###############################################################################
from collections import deque


def solution(n, s, a, b, fares):
    answer = 0
    graph = defaultdict(list)

    # A, B 경로, cost
    root_A, root_B = [], []

    # 그래프 그려주는 함수
    def set_graph(a, b, cost):
        graph[a].append([b, cost])
        graph[b].append([a, cost])

    for n1, n2, cost in fares:
        set_graph(n1, n2, cost)

    # visited = [0 for _ in range(201)]

    def bfs(start, visited="", cost=0):
        q = deque()
        visited = str(start)
        q.append((start, visited, cost))
        while q:
            pos, visited, cost = q.popleft()
            for next in graph[pos]:
                if str(next[0]) not in visited:
                    if next[0] == b:
                        root_B.append((visited + str(next[0]), cost + next[1]))
                        continue
                    if next[0] == a:
                        root_A.append((visited + str(next[0]), cost + next[1]))
                        continue
                    q.append((next[0], visited + str(next[0]), cost + next[1]))

    bfs(s)
    print(sorted(root_A))
    print(sorted(root_B))

    return answer


# solution(n, s, a, b, fares)

###############################################################################
def solution(n, s, a, b, fares):
    start = time.time()
    answer = 0

    # A, B 경로, cost
    root_A, root_B = [], []

    graph = defaultdict(dict)

    # 그래프 그려주는 함수
    def set_graph(a, b, cost):
        graph[a][b] = cost
        graph[b][a] = cost

    for n1, n2, cost in fares:
        set_graph(n1, n2, cost)

    # visited = [0 for _ in range(201)]

    def bfs(start, visited="", cost=0):
        q = deque()
        visited = str(start)
        q.append((start, visited, cost))
        while q:
            pos, visited, cost = q.popleft()
            find_cnt = 0
            for next in graph[pos].keys():
                if str(next) not in visited:
                    if next == b:
                        root_B.append((visited + str(next), cost + graph[pos][next]))
                        find_cnt += 1

                    elif next == a:
                        root_A.append((visited + str(next), cost + graph[pos][next]))
                        find_cnt += 1
                    if find_cnt == 2:
                        continue
                    q.append((next, visited + str(next), cost + graph[pos][next]))

    tmp_time = time.time()
    bfs(s)
    print(time.time() - tmp_time)

    print(sorted(root_A))
    print(sorted(root_B))
    tmp_time = time.time()
    min_cost = inf
    for root_a, cost_a in sorted(root_A):
        for root_b, cost_b in sorted(root_B):
            tmp_cost = 0
            tmp_root = ""
            for idx, (pos_a, pos_b) in enumerate(zip(root_a, root_b)):
                if pos_a != pos_b:
                    if min_cost > cost_a + cost_b - tmp_cost:
                        min_cost = cost_a + cost_b - tmp_cost
                    break
                elif idx == 0:
                    tmp_root += pos_a
                else:
                    tmp_cost += graph[int(tmp_root[-1])][int(pos_a)]
                    tmp_root += pos_a
            else:
                if min_cost > cost_a + cost_b - tmp_cost:
                    min_cost = cost_a + cost_b - tmp_cost
    print(time.time() - tmp_time)
    print(min_cost)
    print(time.time() - start)
    return min_cost


# solution(n, s, a, b, fares)

# 시간 복잡도 초과
##############################################################
"""
1. 시작점 -> 모든 점 최소 요금 경로 다익스트라로 구하기
2. 각 모든 점에서 A, B 로 가는 다익스트라 구하기
"""
"""
문제 : A와 B가 합승하여 요금이 최저인 경로로 갔을 때 비용은?
    n : 지점의 개수
    s : 출발 지점
    a : A의 도착지점
    b : B의 도착지점
    fares : 지점사이의 택시요금 나타냄
"""
n = 6
s = 4
a = 6
b = 2
fares = [
    [4, 1, 10],
    [3, 5, 24],
    [5, 6, 2],
    [3, 1, 41],
    [5, 1, 24],
    [4, 6, 50],
    [2, 4, 66],
    [2, 3, 22],
    [1, 6, 25],
]


def solution(n, s, a, b, fares):
    answer = 0

    graph = defaultdict(list)

    # 그래프 그려주는 함수
    def set_graph(a, b, cost):
        graph[a].append([b, cost])
        graph[b].append([a, cost])

    for f, e, cost in fares:
        set_graph(f, e, cost)

    costs_all = defaultdict(int)
    costs_all_to_B = defaultdict(int)

    # visited 추가해서 두번째 다익스트라에서 중복으로 Q 처리 안하게 하기 - 추가 할것 !!!!

    Q = [(0, s)]
    while Q:
        cost, node = heapq.heappop(Q)
        if not costs_all[node]:
            for next_node, next_cost in graph[node]:
                costs_all[node] = cost
                heapq.heappush(Q, (cost + next_cost, next_node))
    print(costs_all)

    min_cost = costs_all[a] + costs_all[b]
    for i in range(1, n + 1):
        costs_all_to_A = defaultdict(int)
        if i == s:
            continue
        Q = [(0, i)]
        A, B = None, None
        while Q:
            cost, node = heapq.heappop(Q)
            if node == a and A == None:
                A = cost
            if node == b and B == None:
                B = cost
            if A != None and B != None:
                min_cost = min(costs_all[i] + A + B, min_cost)
                break
            if not costs_all_to_A[node]:
                for next_node, next_cost in graph[node]:
                    costs_all_to_A[node] = cost
                    # if not costs_all_to_A[next_node]:
                    heapq.heappush(Q, (cost + next_cost, next_node))
    print(min_cost)

    return min_cost


solution(n, s, a, b, fares)
