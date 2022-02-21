# https://leetcode.com/problems/number-of-islands/

from typing import List

## 내 풀이
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def dfs(v):
            # v : (i,j)
            visited[v[0]][v[1]] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (
                    0 <= dx + v[0] < m
                    and 0 <= dy + v[1] < n
                    and grid[dx + v[0]][dy + v[1]] == "1"
                    and not visited[dx + v[0]][dy + v[1]]
                ):
                    dfs((dx + v[0], dy + v[1]))

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs((i, j))
                    cnt += 1
        print(cnt)
        return cnt


sol = Solution()
sol.numIslands(
    grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)
