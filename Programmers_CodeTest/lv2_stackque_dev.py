from math import ceil


def solution(progresses, speeds):
    answer = []
    # que = []
    cnt = 1
    remain_days = [ceil((100 - i) / j) for i, j in zip(progresses, speeds)]
    print(f'remain_days : {remain_days}')
    while remain_days:
        tmp = remain_days.pop(0)
        _remain_days = remain_days[:]
        for i in remain_days:
            if i <= tmp:
                cnt += 1
                _remain_days.pop(0)
            else:
                break
        answer.append(cnt)
        cnt = 1
        remain_days = _remain_days[:]

    print(answer)
    return answer


solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
