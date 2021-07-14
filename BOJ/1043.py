# https://www.acmicpc.net/problem/1043

N, M = map(int, input().split())
known_people = list(map(int, input().split()))
if known_people[0] != 0:
    known_people = known_people[1:]
people = {}
partys = {}
for party in range(M):
    tmp = list(map(int, input().split()))
    partys[party] = tmp[1:]
    for i in tmp[1:]:
        if i not in people:
            people[i] = [party]
        else:
            people[i].append(party)

stack = known_people[:]
visited = []
tmp = set()
if stack[0] == 0:
    print(M)
else:
    while stack:
        person = stack.pop()
        if person not in visited:
            visited.append(person)
            if person in people:
                tmp |= set(people[person])
                for i in people[person]:
                    stack = list(set(stack) | set(partys[i]))
    print(M-len(tmp))
