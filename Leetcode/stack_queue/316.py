from collections import Counter


class Solution:
    # 풀이 1 : 재귀로 풀기
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char) :]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))
        return ""

    # 풀이 2 : 스택으로 풀기
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = Counter(s), []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue

            # stack의 젤 마지막 문자가 기준 문자(char) 보다 크고 아직 뒤에 또 나올 경우 stack에서 뺴준다.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return "".join(stack)
