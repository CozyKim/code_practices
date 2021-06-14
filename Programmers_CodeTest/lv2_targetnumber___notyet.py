# https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers: list, target):
    answer = 0
    graph = {}
    for idx in range(len(numbers)-1, 0, -1):
        graph[idx+1] = {
            idx: numbers[idx-1], -(idx): -numbers[idx-1]}
        graph[-(idx+1)] = {idx: numbers[idx-1],
                           -(idx): -numbers[idx-1]}
    numbers.append(0)
    graph[len(numbers)] = {len(numbers) - 1: numbers[len(numbers) -
                                                     2], -(len(numbers) - 1): -numbers[len(numbers) - 2]}

    print(graph)
    len_ = len(numbers)
    numbers = [idx for idx in range(-len(numbers)+1, len(numbers)) if idx != 0]
    numbers.append(len_)
    print(numbers)
    numbers.sort(key=lambda x: abs(x))
    print(numbers)
    visted = []
    stack = [numbers.pop()]
    while stack:
        n = stack.pop()
        # if graph[n] not in visted:

    #     c = numbers.pop()
    #     if graph[ ]
    return answer


solution([1, 3, 1, 2, 1], 3)
