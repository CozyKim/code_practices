# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):

    tmp = [0 for _ in range(max(citations)+1)]
    _citation = {}
    while citations:
        n = citations.pop()
        if n not in _citation:
            _citation[n] = 1
        else:
            _citation[n] += 1
    for n in _citation:
        tmp[n] = _citation[n]
    rank = max(_citation.keys())
    N = 0
    answer = rank
    for i in range(rank, -1, -1):
        if i in _citation:
            N += _citation[i]
        if N >= i:
            break
    print(i)
    return i


solution([4, 1, 1, 1, 4])
