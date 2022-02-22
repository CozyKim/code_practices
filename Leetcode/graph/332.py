# https://leetcode.com/problems/reconstruct-itinerary/

from typing import List


from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for s, d in sorted(tickets, reverse=True):
            graph[s].append(d)

        result = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            result.append(start)

        dfs("JFK")
        return result[::-1]


# 풀이 2 스택 사용
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for s, d in sorted(tickets, reverse=True):
            graph[s].append(d)
        route, stack = [], ["JFK"]
        while stack:
            # 반복으로 스택을 구성하되 막ㅎ ㅣ는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        # 다시 뒤집어서 어순 결과로
        return route[::-1]


sol = Solution()
print(
    sol.findItinerary(
        tickets=[
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
    )
)
