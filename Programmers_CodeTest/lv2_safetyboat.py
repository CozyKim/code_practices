# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

def solution(people: list, limit: int):
    answer = 0
    people.sort()
    while people:
        n = people.pop()
        for idx, i in enumerate(people):
            if limit - n >= i:
                if idx != len(people) - 1:
                    people = people[:idx] + people[idx+1:]
                else:
                    people = people[:idx]
                break
        answer += 1
    # print(answer)
    return answer


solution([70, 80, 50]	, 100)
