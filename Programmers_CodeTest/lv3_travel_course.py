# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3


def solution(tickets: list):
    answer = []
    tmp = []

    def DFS(start, end, idx_list=[]):
        check = [0] * len(tickets)
        for i in idx_list:
            check[i] = 1
        if sum(check) == len(tickets):
            tmp.append([tickets[i][0] for i in idx_list])
            tmp[-1].append(tickets[idx_list[-1]][1])
            return
        for idx, (next_start, next_end) in enumerate(tickets):
            if end == next_start and check[idx] == 0:

                DFS(next_start, next_end, idx_list + [idx])

    for idx, (a, b) in enumerate(tickets):
        if a == 'ICN':
            start = a
            end = b
            DFS(start, end, [idx])
            answer += tmp
            tmp = []
    print(min(answer))
    return min(answer)


solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]])
