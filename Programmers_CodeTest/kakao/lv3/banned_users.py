# https://programmers.co.kr/learn/courses/30/lessons/64064


import re


def solution(user_id, banned_id):
    candidate = [[] for _ in range(len(banned_id))]
    for i, ban_id in enumerate(banned_id):
        ban_id = ban_id.replace("*", "[\w]")
        for j, user in enumerate(user_id):
            if re.match(ban_id + "$", user):
                candidate[i].append(j)
    visited = [0] * len(user_id)

    def dfs(idx, visited):
        nonlocal answer
        if idx == len(candidate):
            answer.add(tuple([i + 1 for i in range(len(visited)) if visited[i]]))
            return

        for i in candidate[idx]:
            if not visited[i]:
                visited[i] = 1
                dfs(idx + 1, visited)
                visited[i] = 0

    answer = set()
    for i in candidate[0]:
        visited[i] = 1
        dfs(1, visited)
        visited[i] = 0
    return len(answer)


print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"],
    )
)
