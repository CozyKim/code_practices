# https://www.acmicpc.net/problem/2263

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

position = [0] * (n + 1)

for i in range(n):
    position[in_order[i]] = i

# 분할 정복 방식으로 전위 순회 찾음
def pre_order(in_s, in_e, po_s, po_e):
    # 수렴 조건
    if (in_s > in_e) or (po_s > po_e):
        return

    # post_order의 마지막 부분은 서브 트리의 부모이다
    parent = post_order[po_e]
    print(parent, end=" ")

    # in_order에서 부모(root)를 중심으로 좌, 우 서브트리로 나뉜다
    left = position[parent] - in_s
    right = in_e - position[parent]

    # 좌, 우 서브 트리로부터 다시 분할 정복으로 트리 추적하여 전위 순회 찾음
    pre_order(in_s, in_s + left - 1, po_s, po_s + left - 1)
    pre_order(in_e - right + 1, in_e, po_e - right, po_e - 1)


pre_order(0, n - 1, 0, n - 1)
