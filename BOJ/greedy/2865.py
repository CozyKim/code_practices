import sys
from collections import defaultdict
input = sys.stdin.readline
result = 0
N, M, K = map(int, input().rstrip().split())

people_max_gerne = defaultdict(int)
for gerne in range(M):
    line = list(map(float, input().rstrip().split()))
    for i in range(len(line)):
        if i % 2 == 0:
            people_max_gerne[int(line[i])] = max(
                people_max_gerne[int(line[i])], line[i+1])
for idx, (_, v) in enumerate(sorted(people_max_gerne.items(), key=lambda x: x[1], reverse=True)):
    if idx < K:
        result += v
    else:
        break
print(round(result, 1))
