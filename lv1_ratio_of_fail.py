def solution(N, stages):
    answer = []
    _stages = {i: 0 for i in range(1, N+2)}
    for s in stages:
        _stages[s] += 1
    for s in range(1, N+1):
        answer.append([s, ratio_fail(s, _stages)])
    answer.sort()
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    a = [i for i, _ in answer]
    return [i for i, _ in answer]


def ratio_fail(stage: int, all: dict):
    return 0 if sum(list(all.values())[stage-1:]) == 0 else list(all.values())[stage-1] / sum(list(all.values())[stage-1:])


solution(4, [4, 4, 4, 4])
