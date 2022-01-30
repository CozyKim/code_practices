# https://leetcode.com/problems/daily-temperatures/


class Solution:
    # 나의 풀이
    def dailyTemperatures(self, temperatures):
        result = [0 for _ in range(len(temperatures))]
        stack = []
        idx_to_tmp = {}
        for idx, tmp in enumerate(temperatures):
            idx_to_tmp[idx] = tmp

            while stack and idx_to_tmp[stack[-1]] < tmp:
                tmp_idx = stack.pop()
                result[tmp_idx] = idx - tmp_idx
            else:
                stack.append(idx)
        return result


sol = Solution()
sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
