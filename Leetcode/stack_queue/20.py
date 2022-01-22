# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        mapping_table = {")": "(", "}": "{", "]": "["}
        stack = []
        for brackect in s:
            if brackect not in mapping_table:
                stack.append(brackect)
            elif not stack or mapping_table[brackect] != stack.pop():
                return False
        return len(stack) == 0
