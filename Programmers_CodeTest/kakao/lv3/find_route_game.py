# https://programmers.co.kr/learn/courses/30/lessons/42892


from collections import defaultdict


def solution(nodeinfo):
    answer = []
    node_info = [[l, idx + 1] for idx, l in enumerate(nodeinfo)]
    # print(nodeinfo)
    node_info = sorted(node_info, key=lambda x: (x[0][1], -x[0][0]), reverse=True)
    print(node_info)
    graph = defaultdict(lambda: [0, 0])

    def make_graph(node, goal):
        if nodeinfo[node - 1][0] > nodeinfo[goal - 1][0]:
            if not graph[node][0]:
                graph[node][0] = goal
                return
            make_graph(graph[node][0], goal)
        else:
            if not graph[node][1]:
                graph[node][1] = goal
                return
            make_graph(graph[node][1], goal)

    parent = node_info[0][1]
    for node_pos, value in node_info:
        if value == parent:
            continue
        make_graph(parent, value)
    print(graph)

    # front search
    f_list = []

    def dfs_f(node):
        if node == 0:
            return
        f_list.append(node)
        for n_node in graph[node]:
            dfs_f(n_node)

    dfs_f(parent)
    print(f_list)

    # last search
    l_list = []

    def dfs_l(node):
        if node == 0:
            return
        for n_node in graph[node]:
            dfs_l(n_node)
        l_list.append(node)

    dfs_l(parent)
    print(l_list)
    answer.append(f_list)
    answer.append(l_list)
    return answer


solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
