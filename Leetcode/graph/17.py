# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_str = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []

        def dfs(pos=0, tmp=""):
            if pos == len(digits):
                result.append(tmp)
                return
            for alpha in num_to_str[digits[pos]]:
                dfs(pos + 1, tmp + alpha)

        if digits:
            dfs()
        return result


sol = Solution()
print(sol.letterCombinations(digits=""))
