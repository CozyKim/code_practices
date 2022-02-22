# https://leetcode.com/problems/course-schedule/

from typing import List


from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        global traced, visited
        traced = set()
        visited = set()

        def dfs(start):
            global traced
            # 순환 구조이면 False
            if start in traced:
                return False

            # 이미 방문한 이력이 있으면 True (순환구조였으면 위에서 걸러짐)
            if start in visited:
                return True

            traced |= {
                start,
            }

            for next in graph[start]:
                if not dfs(next):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced -= {
                start,
            }

            # 탐색 종료 후 방문 노드 추가
            visited.add(start)
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True


sol = Solution()
print(sol.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
