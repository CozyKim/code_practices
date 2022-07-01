# https://programmers.co.kr/learn/courses/30/lessons/87377


def solution(line):
    answer = set()
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            if not A * D - B * C:
                continue
            x, y = (B * F - E * D) / (A * D - B * C), (E * C - A * F) / (A * D - B * C)
            if x == int(x) and y == int(y):
                answer.add((int(x), int(y)))
    # print(answer)
    bias_u = max(answer, key=lambda x: x[1])[1]
    bias_l = min(answer, key=lambda x: x[0])[0]
    bias_r = max(answer, key=lambda x: x[0])[0]
    bias_d = min(answer, key=lambda x: x[1])[1]
    result = [["."] * (bias_r - bias_l + 1) for _ in range(bias_u - bias_d + 1)]
    for c, r in answer:
        result[bias_u - r][c - bias_l] = "*"
    answer = ["".join(line) for line in result]
    # print(answer)
    return answer


solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[1, -1, 0], [2, -1, 0]])
solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
