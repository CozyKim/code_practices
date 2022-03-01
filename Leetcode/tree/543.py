# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(node):
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드 까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.max_length = max(self.max_length, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.max_length
