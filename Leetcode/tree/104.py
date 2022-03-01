# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

# 내가 푼 풀이
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            q = deque([])
            q.append((root, 1))
            max_depth = 0
            while q:
                node, depth = q.popleft()
                max_depth = max(max_depth, depth)
                if node.left != None:
                    q.append((node.left, depth + 1))
                if node.right != None:
                    q.append((node.right, depth + 1))
            return max_depth

        if root:
            return bfs(root[0])
        else:
            return 0

    # 책에서 제시한 풀이
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연ㅏ 추ㄹ 노의 자ㄱ 노 삽ㅣ
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 판복 횟수 == 깊이
        return depth
