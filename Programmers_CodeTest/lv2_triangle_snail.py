
# https://programmers.co.kr/learn/courses/30/lessons/68645


from collections import deque


def solution(n):
    answer = []
    case = deque([[i]+[0]*(i-1) for i in range(1, n+1)])
    print(case)
    answer.append(case.popleft())
    up = 1
    num = n+1
    while case:
        if up:
            for layer in range(len(case)-1, -1, -1):
                if layer == len(case) - 1:
                    for idx, i in enumerate(case[layer]):
                        if i == 0:
                            case[layer][idx] = num
                            num += 1
                else:
                    for i in range(len(case[layer])-1, -1, -1):
                        if case[layer][i] == 0:
                            case[layer][i] = num
                            num += 1
                            break

            answer.append(case.popleft())
            if case:
                answer.append(case.pop())
            up = 0

        else:
            for layer in range(len(case)):
                for i in range(1, len(case[layer])):
                    if case[layer][i] == 0:
                        case[layer][i] = num
                        num += 1
                        break
            up = 1
            answer.append(case.popleft())
    answer.sort()
    A = []
    for i in answer:
        A += i
    print(A)
    return A


solution(1000)
