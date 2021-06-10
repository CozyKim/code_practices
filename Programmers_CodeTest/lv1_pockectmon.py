def solution(nums):

    _nums = set(nums)

    return len(_nums) if len(nums) / 2 >= len(_nums) else len(nums) / 2
