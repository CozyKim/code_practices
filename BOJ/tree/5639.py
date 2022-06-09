from collections import defaultdict
import sys

input = sys.stdin.readline
nodes = []
while 1:
    try:
        nodes.append(int(input()))
    except:
        break

tree = defaultdict(lambda: [None, None])
stack = [nodes[0]]
for node in nodes[1:]:
    if stack[-1] > node:
        tree[stack[-1]][0] = node
    elif stack[-1] < node:
        while stack and stack[-1] < node:
            check_node = stack.pop()
        tree[check_node][1] = node
    stack.append(node)
print(tree)


def dfs(node):
    if node not in tree:
        return node

    for next_node in tree[node]:
        if next_node == None:
            continue
        print(dfs(next_node))
    return node


print(dfs(nodes[0]))
