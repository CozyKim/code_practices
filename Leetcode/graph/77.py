# https://leetcode.com/problems/combinations/

from typing import List

# 풀이 1. itertools 사용

from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1, n + 1), k)))


# 풀이 2. DFS로 풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # n = range(1, n+1)
        result = []

        def dfs(start, visited):
            if len(visited) == k:
                result.append(visited)
                return
            for i in range(start + 1, n + 1):
                if i not in visited:
                    dfs(i, visited + [i])

        for i in range(1, n + 1):
            dfs(i, [i])
        return result


# 풀이 3. 책에서 제한하는 DFS풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                result.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result


sol = Solution()
print(sol.combine(n=4, k=2))
