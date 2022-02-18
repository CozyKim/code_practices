# https://leetcode.com/problems/jewels-and-stones/

import collections

# 나의 풀이


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnter = collections.Counter(stones)
        result = 0
        for j in jewels:
            result += cnter[j]

        return result


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
