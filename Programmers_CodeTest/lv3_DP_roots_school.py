# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3
def solution(m, n, puddles):
    answer = 0
    dp = {}
    puddle = [(x-1, y-1) for x, y in puddles]
    for i in range(n):
        for j in range(m):
            if (i, j) in puddle:
                dp[(i, j)] = 0
            else:
                if i == 0 and j == 0:
                    dp[(0, 0)] = 1
                elif i == 0 and j != 0:
                    dp[(i, j)] = dp[(i, j-1)]
                elif i != 0 and j == 0:
                    dp[(i, j)] = dp[(i-1, j)]
                else:
                    dp[(i, j)] = dp[(i-1, j)] + dp[(i, j-1)]
    answer = dp[(n-1, m-1)]
    print(answer)
    return answer


solution(4, 3, [[2, 2]])
