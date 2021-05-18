import sys
lst = []
cnt = 1


N = int(sys.stdin.readline())
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lst.append([start, end])
lst.sort()
lst.sort(key=lambda x: x[1])
end_check = lst[0][1]
if lst[0][0] == lst[0][1]:
    cnt -= 1
for start_, end_ in lst:
    if start_ >= end_check:
        cnt += 1
        end_check = end_
print(cnt)
