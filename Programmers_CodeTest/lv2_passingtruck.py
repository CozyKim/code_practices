# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting_truck = deque(truck_weights)
    passing_truck = deque([])
    passed_truck = []
    flag = 1
    time = deque([])
    while len(passed_truck) != len(truck_weights):
        if flag and len(waiting_truck) != 0:
            n = waiting_truck.popleft()
        if len(passing_truck) != 0 and answer != 0 and time[0] == bridge_length:
            passed_truck.append(passing_truck.popleft())
            time.popleft()
        if sum(passing_truck) + n <= weight and len(passing_truck) + 1 <= bridge_length:
            passing_truck.append(n)
            time.append(0)
            flag = 1
        else:
            flag = 0
        answer += 1
        for i in range(len(time)):
            time[i] += 1
    return answer


solution(2, 10, [7, 4, 5, 6])
