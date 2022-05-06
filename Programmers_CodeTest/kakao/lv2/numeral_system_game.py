# https://programmers.co.kr/learn/courses/30/lessons/17687


def solution(n, t, m, p):
    answer = ""

    def n_to_numeral(origin, n):
        result = ""
        while origin > 0:
            origin, b = divmod(origin, n)
            if b >= 10:
                b = chr(ord("A") + b - 10)
            result += str(b)
        if result:
            return result[::-1]
        else:
            if origin >= 10:
                return chr(ord("A") + origin - 10)
            return str(origin)

    result = ""
    num = 0
    while len(result) < t * m:
        print(n_to_numeral(num, n))
        result += n_to_numeral(num, n)
        num += 1
    cnt = 0
    idx = p - 1
    while cnt < t:
        answer += result[idx]
        idx += m
        cnt += 1

    return answer


solution(16, 16, 2, 2)
