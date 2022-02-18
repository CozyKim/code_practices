# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
import collections

# 내 풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        result = []
        for idx, (key, v) in enumerate(
            sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ):
            if idx + 1 == k:
                result.append(key)
                return result
            result.append(key)


# 힙 사용
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        result = []
        freq_heap = []
        for f in freq:
            heapq.heappush(freq_heap, (-freq[f], f))
        for _ in range(k):
            result.append(heapq.heappop(freq_heap)[1])
        return result


# Pythonic
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
