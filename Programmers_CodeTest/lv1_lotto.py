def solution(lottos: list, win_nums):
    answer = []
    zeors = lottos.count(0)
    check = [n for n in lottos if n in win_nums]
    if 7-len(check)-zeors > 5:
        answer.append(6)
        answer.append(6)
    elif 7-len(check) > 5:
        answer.append(7-len(check)-zeors)
        answer.append(6)
    else:
        answer.append(7-len(check)-zeors)
        answer.append(7-len(check))
    return answer
