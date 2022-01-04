# https://leetcode.com/problems/group-anagrams/
from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for str in strs:
            anagrams["".join(sorted(str))].append(str)
        return list(anagrams.values())


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
