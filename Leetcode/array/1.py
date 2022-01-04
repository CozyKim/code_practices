# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
            check = target - n
            if check in nums[idx + 1 :]:
                return [idx, idx + 1 + nums[idx + 1 :].index(check)]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, n in enumerate(nums):
            nums_map[n] = idx
        for idx, n in enumerate(nums):
            if target - n in nums_map and idx != nums_map[target - n]:
                return [idx, nums_map[target - n]]


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
