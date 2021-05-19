import sys


N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort()
tmp = P[0]
times = [tmp]
for i in range(N-1):
    time = tmp + P[i+1]
    tmp = time
    times.append(time)
print(sum(times))
