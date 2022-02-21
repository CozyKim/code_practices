# https://leetcode.com/problems/permutations/
from typing import List


# itertools 사용 (내 풀이)
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations(nums, len(nums))))


# DFS 사용


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(visited=[nums[0]]):

            if len(visited) == len(nums):
                result.append(visited)
                return

            for i in range(len(nums)):
                if nums[i] not in visited:
                    dfs(visited + [nums[i]])

        for i in range(len(nums)):
            dfs([nums[i]])
        return result


sol = Solution()
print(sol.permute([1, 2, 3]))
