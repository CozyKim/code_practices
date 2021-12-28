# https://www.acmicpc.net/problem/5014
"""
문제 설명
스타트 링크 : 총 F층으로 이뤄진 고층 건물에 사무실이 있고 스타트링크가 있는 곳의 위치는 G층
강호가 지금 있는 곳은 S층, 엘리베이터를 타고 G층으로 이동하려함
엘리베이터는 위로 U층으로 가는 버튼과 아래로 D층 가는 버튼 밖에 존재 안함, 
U층위 D층아래 해당하는 층이 없을 때는 엘리베이터는 움직이지 않음
강호가 G층에 도착하려면 버튼을 적어도 몇 번 눌러야하는지 ?
갈 수 없다면 use the stairs 출력
"""

from collections import deque

# 첫째 줄에 F,S,G,U,D 존재
F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F + 1)]

CNT = 0


def bfs():
    q = deque()
    q.append((S, CNT))
    if S == G:
        return 0
    while q:
        pos, cnt = q.popleft()

        # 엘리베이터 다음 이동 할 곳이 G 층이라면 몇 번 움직였는지 출력
        if pos + U == G or pos - D == G:
            return cnt + 1

        if pos + U <= F:
            if not visited[pos + U]:
                visited[pos + U] = 1
                q.append((pos + U, cnt + 1))
        if pos - D > 1:
            if not visited[pos - D]:
                visited[pos - D] = 1
                q.append((pos - D, cnt + 1))
    return "use the stairs"


print(bfs())
