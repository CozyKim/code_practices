# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    answer = 0
    dp = {}
    for i in range(len(triangle)):
        for j in range(i+1):
            if i == 0:
                dp[(i, j)] = triangle[i][j]
            elif j == 0:
                dp[(i, j)] = dp[(i-1, j)] + triangle[i][j]
            elif j == i:
                dp[(i, j)] = dp[(i-1, j-1)] + triangle[i][j]
            else:
                dp[(i, j)] = max(dp[(i-1, j-1)] + triangle[i]
                                 [j], dp[(i-1, j)] + triangle[i][j])

    answer = max(dp.values())
    return answer


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
