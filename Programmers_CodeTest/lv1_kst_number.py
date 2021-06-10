def solution(array: list, commands):
    answer = []
    for com in commands:
        _array = array[:]
        _array = _array[com[0]-1:com[1]]
        _array.sort()
        answer.append(_array[com[2]-1])
    return answer
