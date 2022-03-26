# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
from collections import deque
import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        result = ["#"]
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append("#")
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 예외 처리
        if data == "# #":
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐에 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] != "#":
                node.left = TreeNode(nodes[index])
                queue.append(node.left)

            index += 1

            if nodes[index] != "#":
                node.right = TreeNode(nodes[index])
                queue.append(node.right)

            index += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
