# https://programmers.co.kr/learn/courses/30/lessons/62048


def solution(w, h):
    answer = w * h
    # 최대 공약수로 나눈 크기를 구해야 한다.
    a, b = max(w, h), min(w, h)
    while b:
        a, b = b, a % b
    print(a)
    w, h = w // a, h // a
    answer -= a * (w + h - 1)
    print(answer)
    return answer


solution(8, 12)
