# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for idx, char in enumerate(s):
            # 이미 등장 했다면 start 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)

            used[char] = idx
        return max_length
