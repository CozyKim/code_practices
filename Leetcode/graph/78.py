# https://leetcode.com/problems/subsets/

from typing import List

# 나의 풀이
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def dfs(element, start):
            if len(element) == len(nums):
                return
            for i in range(start, len(nums)):
                result.append(element + [nums[i]])
                dfs(element + [nums[i]], i + 1)

        dfs([], 0)
        return result


sol = Solution()
print(sol.subsets(nums=[1, 2, 3]))
