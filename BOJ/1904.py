# https://www.acmicpc.net/problem/1904


N = int(input())
tl = [0] * 1000001
tl[1], tl[2] = 1, 2
for i in range(3, N+1):
    tl[i] = (tl[i-1] + tl[i-2]) % 15746
print(tl[N])

# 메모리 초과 -> for 문 안에서 나머지 연산을 해야함
