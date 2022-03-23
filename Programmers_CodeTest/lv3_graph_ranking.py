# https://programmers.co.kr/learn/courses/30/lessons/49191

from collections import defaultdict


def solution(n, results):
    answer = 0
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    for w, l in results:
        win_graph[l].append(w)
        lose_graph[w].append(l)

    wins = set()
    loses = set()

    def dfs(node, win):
        if win:
            if node in wins:
                return
            wins.add(node)
            for next_node in win_graph[node]:
                if next_node not in wins:
                    dfs(next_node, win)
        else:
            if node in loses:
                return
            loses.add(node)
            for next_node in lose_graph[node]:
                if next_node not in loses:
                    dfs(next_node, win)

    for i in range(1, n + 1):
        dfs(i, True)
        dfs(i, False)
        if len(wins) + len(loses) - 2 == n - 1:
            answer += 1
        wins = set()
        loses = set()
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
