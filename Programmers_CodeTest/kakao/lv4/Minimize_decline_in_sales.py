# https://programmers.co.kr/learn/courses/30/lessons/72416
"""
제한
    한 직원은 최대 2개의 팀에 소속
    
    부모 노드 : 팀장
    자식 노드 : 팀원

    반드시 팀 하나에는 팀원과 팀장있다.

    트리 구조를 이루고 있다.

    루트 노드는 CEO

    모든 팀에서 최소 1명 이상 직원 참석, 직원들 하루평균 매출액 합 최소
"""

from collections import defaultdict


def solution(sales, links):
    graph = defaultdict(list)

    for a, b in links:
        graph[a - 1].append(b - 1)

    dp = [[0, 0] for _ in range(len(sales))]

    def dfs(node):
        dp[node][1] = sales[node]
        if node not in graph:
            return
        tmp = 0
        other = float("inf")
        add_other = True
        for next_node in graph[node]:
            dfs(next_node)
            tmp += min(dp[next_node][0], dp[next_node][1])
            other = min(other, dp[next_node][1] - dp[next_node][0])
            if dp[next_node][0] > dp[next_node][1]:
                add_other = False
        dp[node][1] = sales[node] + tmp
        dp[node][0] = tmp + other if add_other else tmp

    dfs(0)
    return min(dp[0][1], dp[0][0])


solution([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]])
solution(
    [14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
    [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]],
)
