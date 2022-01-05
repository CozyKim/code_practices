# https://leetcode.com/problems/3sum/
from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_mapping = defaultdict(int)
        result = defaultdict(int)

        for num in nums:
            num_mapping[num] += 1

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                check = 0 - (nums[i] + nums[j])
                check_num = 1
                if nums[i] == check:
                    check_num += 1
                if nums[j] == check:
                    check_num += 1
                if (
                    num_mapping[check] >= check_num
                    and not result[tuple(sorted([nums[i], nums[j], check]))]
                ):
                    result[tuple(sorted([nums[i], nums[j], check]))] = 1

        return list(list(k) for k in result.keys())

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


sol = Solution()
print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
