from collections import deque


def solution(priorities, location):
    answer = 1
    tmp = [[priorities[i], 0] for i in range(len(priorities))]
    # _location[location] = 1
    # position = 0
    tmp[location][1] = 1
    _priorities = deque(tmp)
    _max = max(_priorities)[0]
    while (_priorities[0][1] != 1) or (_max != _priorities[0][0]):
        n, pos = _priorities.popleft()
        if n == _max:
            answer += 1
        else:
            _priorities.append([n, pos])
        _max = max(_priorities)[0]
    return answer


solution([1, 1, 9, 1, 1, 1], 0)
