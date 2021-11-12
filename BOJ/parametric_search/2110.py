"""
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
"""

"""
입력 : 집의 개수 N, 공유기의 개수 C 
      집의 좌표 x_i
출력 : 가장 입접한 두 공유기 사이의 최대 거리
"""


"""
pseudo code
1. 가장 인접한 공유기의 거리 범위는 1 ~ (max(x_i들) + min(x_i들)) // (C-1)
"""

import sys

input = sys.stdin.readline

N, C = map(int, input().strip().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
right = (house[-1] - house[0]) // (C - 1)
left = 1

while left <= right:
    mid = (left + right) // 2
    start = house[0]
    cnt = 1

    for i in range(1, N):
        d = house[i] - start
        if mid <= d:
            cnt += 1
            start = house[i]

    if cnt >= C:
        # 공유기 수를 줄여라
        ans = mid
        left = mid + 1
    else:
        # 공유기가 더 설치 되어야 한다
        right = mid - 1
print(ans)
