# https://www.acmicpc.net/problem/2565

import sys

input = sys.stdin.readline

N = int(input())
elec_line = sorted([list(map(int, input().split())) for _ in range(N)])
dp = [1] * N

"""
첫번째 전깃줄에 대해 정렬 했을 때 두번째 전기줄도 같이 오름차순으로 나와야 겹치지 않는 것이다.
결국 겹치지 않는 최대 전기줄의 수는 기준(i) 보다 작은 값(j) 에 대해 "부분 증가 수열의 최대 길이"와 같다
"""

for i in range(N):
    for j in range(i):
        if elec_line[i][1] > elec_line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
