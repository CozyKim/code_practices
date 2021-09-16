import sys
input = sys.stdin.readline
N = int(input())
answer = [0]*(1001)
assignments = []
for _ in range(N):
    deadline, score = map(int, input().rstrip().split())
    assignments.append((deadline, score))

assignments = sorted(assignments, key=lambda x: x[1], reverse=True)
for deadline, score in assignments:
    for i in range(deadline, 0, -1):
        if answer[i] == 0:
            answer[i] = score
            break

print(sum(answer))
