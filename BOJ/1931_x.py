import sys
lst = []
cnt = []


N = int(sys.stdin.readline())
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lst.append([start, end])
lst.sort()
for i in range(N):
    sub_cnt = 1
    for k in range(i, N):
        if lst[i][1] <= lst[k][0]:
            sub_cnt += 1
            i = k
    cnt.append(sub_cnt)
print(max(cnt))
