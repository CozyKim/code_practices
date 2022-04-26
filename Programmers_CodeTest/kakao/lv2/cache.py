# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import defaultdict, deque


def solution(cacheSize, cities):
    answer = 0
    q_set = defaultdict(int)
    for i, city in enumerate(cities):
        city = city.lower()
        if city in q_set:
            answer += 1

        else:
            answer += 5
        q_set[city] = i
        if len(q_set) > cacheSize:
            del_city, _ = min(q_set.items(), key=lambda x: x[1])
            print(f"del_city : {del_city}")
            q_set.pop(del_city)

    print(answer)
    return answer


# solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(
    3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
)
