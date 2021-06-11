def solution(n):
    answer = ''
    nara124_point = []
    i = 1
    tran = {1: 1, 2: 2, 3: 4}
    while i <= n:
        nara124_point.append(i)
        i *= 3
    nara124_point.sort(reverse=True)
    i = 1
    for idx, check in enumerate(nara124_point):
        if idx == len(nara124_point)-1:
            answer += str(tran[n])
        else:
            while n > check*i:
                if sum(nara124_point[idx+1:]) <= n - check*i <= (sum(nara124_point[idx:])-1):
                    answer += str(tran[i])
                    n -= check*i
                    i = 1
                else:
                    i += 1
    return answer


def solution(n):
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


solution(16)
