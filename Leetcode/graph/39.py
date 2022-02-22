# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(basket, s, start):
            if s > target:
                return
            elif s == target:
                result.append(basket[:])
                return
            for i in range(start, len(candidates)):
                basket.append(candidates[i])
                dfs(basket, s + candidates[i], i)
                basket.pop()

        dfs([], 0, 0)
        return result


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(basket, s, start):
            if s > target:
                return
            elif s == target:
                result.append(basket)
                return
            for i in range(start, len(candidates)):
                dfs(basket + [candidates[i]], s + candidates[i], i)

        dfs([], 0, 0)
        return result


sol = Solution()
print(sol.combinationSum(candidates=[2, 3, 6, 7], target=7))
