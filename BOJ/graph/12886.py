
from collections import deque


def is_same(a, b, c):
    if a == b == c:
        return True
    return False


def operator(a, b):
    if a > b:
        a -= b
        b *= 2
    elif a < b:
        b -= a
        a *= 2
    return a, b


def edge_case(a, b, c):
    if sum([a, b, c]) % 3 != 0:
        return True
    return False


def bfs(a, b, visited=[[]], sum=0):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        z = sum - x - y
        if is_same(x, y, z):
            print(1)
            return
        for i, j in (x, y), (y, z), (x, z):
            i, j = operator(i, j)
            k = sum - i - j
            X, Y = min(i, j, k), max(i, j, k)
            if not visited[X][Y]:
                q.append((X, Y))
                visited[X][Y] = True
    print(0)


def solution():
    A, B, C = map(int, input().split())
    sum_nums = sum([A, B, C])
    visited = [[False] * sum_nums for _ in range(sum_nums)]
    if edge_case(A, B, C):
        return print(0)

    if is_same(A, B, C):
        return print(1)
    bfs(A, B, visited, sum_nums)


solution()
# while q:
#     a, b, c = q.popleft()
#     tmp = []
#     tmp.append(list(operator(a, c))+[b])
#     tmp.append(list(operator(a, b))+[c])
#     tmp.append(list(operator(b, c))+[a])
#     for x, y, z in tmp:
#         if is_same(a, b, c):
#             return print(1)
#         result = sorted([x, y, z])
#         if result[1] == tagetnum:
#             if dfs(result, visited):
#                 return print(1)
#         else:
#             if result not in visited:
#                 q.append(result)
#                 visited.append(result)
# return print(0)

# while q:
#     a, b, c = q.popleft()
#     a, c = operator(a, c)
#     result = sorted([a, b, c])
#     if is_same(a, b, c):
#         return print(1)
#     else:
#         if result not in visited and 0 not in result:
#             q.append(result)
#             visited.append(result)

# return print(0)


# def list_of_chosen_num(a, b, c):
#     if a == b:
#         return [[(b, c), a]]
#     elif b == c:
#         return [[(a, c), b]]
#     elif a == c:
#         return [[(b, c), c]]
#     else:
#         all = set([a, b, c])
#         num_list = []
#         for x, y in set(combinations([a, b, c], 2)):
#             left = list(all - {x, y})
#             num_list.append([(x, y), left[0]])
#         return num_list

# def solution():
#     A, B, C = map(int, input().split())
#     nums = set([A, B, C])
#     if edge_case(A, B, C):
#         return print(0)
#     if is_same(A, B, C):
#         return print(1)
#     pres_min, pres_max = min(nums), max(nums)
#     last_min, last_max = 0, inf
#     while last_min != pres_min or last_max != pres_max:
#         a, b = operator(pres_min, pres_max)
#         nums -= set([pres_max])
#         nums -= set([pres_min])
#         nums |= set([a])
#         nums |= set([b])
#         if len(nums) == 1:
#             return print(1)
#         last_min, last_max = pres_min, pres_max
#         pres_min, pres_max = min(nums), max(nums)
#     return print(0)

"""
    음.. 크기가 같지 않은 두 그룹을 고른다...
    작은쪽, X 큰쪽 Y
    20 15 25
    20 30 10
    20 20 20
"""
