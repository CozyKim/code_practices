# https://programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]

    def getParent(x):
        if parent[x] == x:
            return x
        return getParent(parent[x])

    def UnionParent(x, y):
        p_x = getParent(x)
        p_y = getParent(y)
        if p_y > p_x:
            parent[p_y] = p_x
        else:
            parent[p_x] = p_y

    def isSameParent(x, y):
        p_x = getParent(x)
        p_y = getParent(y)
        if p_x == p_y:
            return True
        return False

    costs = sorted(costs, key=lambda x: x[2])
    for a, b, cost in costs:
        if isSameParent(a, b):
            continue
        answer += cost
        UnionParent(a, b)

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
