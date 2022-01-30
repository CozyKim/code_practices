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

    # 책에서 제안한 풀이
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


# .... index로 처리했기 때문에 dict가 필요 없었다..


sol = Solution()
sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
