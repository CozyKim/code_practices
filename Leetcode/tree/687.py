# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    # 내가 푼 풀이
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_cnt = 0
        if not root:
            return 0

        def dfs(node):
            l_val = r_val = None
            l_cnt = r_cnt = 0
            if not node.left and not node.right:
                return node.val, 0

            if node.left:
                l_val, l_cnt = dfs(node.left)
            if node.right:
                r_val, r_cnt = dfs(node.right)

            if l_val == r_val == node.val:
                self.max_cnt = max(self.max_cnt, l_cnt + r_cnt + 2)
                return node.val, max(l_cnt, r_cnt) + 1
            elif r_val == node.val:
                self.max_cnt = max(self.max_cnt, r_cnt + 1)
                return node.val, r_cnt + 1
            elif l_val == node.val:
                self.max_cnt = max(self.max_cnt, l_cnt + 1)
                return node.val, l_cnt + 1
            else:
                self.max_cnt = max(self.max_cnt, l_cnt, r_cnt)
                return node.val, 0

        dfs(root)
        return self.max_cnt

    # 책의 풀이
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_cnt = 0

        def dfs(node):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 압 최댓값이 결과
            self.max_cnt = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.max_cnt
