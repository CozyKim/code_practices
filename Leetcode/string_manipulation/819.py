# https://leetcode.com/problems/most-common-word/
import re
from typing import List
from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pre_words = [word for word in re.sub("[\W]", " ", paragraph.lower()).split()]
        cnt_dict = self.count_words(pre_words)
        for k, v in sorted(cnt_dict.items(), key=lambda x: x[1], reverse=True):
            if k not in banned:
                return k
        return pre_words

    def count_words(self, words: List[str]) -> dict:
        cnt = defaultdict(int)
        for word in words:
            cnt[word] += 1
        return cnt


aa = Solution()
print(
    aa.mostCommonWord(
        paragraph="a, a, b,b,b,a, a",
        banned=["hit"],
    )
)
