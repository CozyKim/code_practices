def solution(absolutes, signs):
    answer = 0
    for n, s in zip(absolutes, signs):
        if not s:
            answer -= n
        else:
            answer += n
    return answer
