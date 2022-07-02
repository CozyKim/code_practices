def solution(a):
    answer = set()
    min_left = [a[0]] * len(a)
    min_right = [a[-1]] * len(a)
    for i in range(1, len(a)):
        min_left[i] = min(min_left[i - 1], a[i - 1])
        min_right[len(a) - 1 - i] = min(min_right[len(a) - i], a[len(a) - i])

    for i in range(len(a)):
        answer.add(min_left[i])
        answer.add(min_right[i])
    return len(answer)
