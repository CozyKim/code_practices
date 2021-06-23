# https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3


def solution(genres, plays):
    answer = []

    _gen = {}  # 장르 : {플레이수 : [고유번호], 플레이수 : [고유번호]}
    order = {}
    for gen in set(genres):
        order[gen] = 0
    for i, (gen, play) in enumerate(zip(genres, plays)):
        order[gen] += play
        if gen not in _gen:
            _gen[gen] = {play: [i]}
        elif play not in _gen[gen]:
            _gen[gen][play] = [i]
        else:
            _gen[gen][play].append(i)

    for gen, _ in sorted(order.items(), key=lambda x: x[1], reverse=True):
        cnt = 0
        for i in sorted(_gen[gen].keys(), reverse=True):
            if cnt == 2:
                break
            if len(_gen[gen][i]) == 1:
                answer += _gen[gen][i]
                cnt += 1
            else:
                answer += sorted(_gen[gen][i])[:2 - cnt]
                cnt = 2
    print(answer)
    return answer


solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
