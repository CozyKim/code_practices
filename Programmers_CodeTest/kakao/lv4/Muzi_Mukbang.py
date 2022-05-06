# https://programmers.co.kr/learn/courses/30/lessons/42891

"""
    음식 이 사라지는 순서는 food_times 작은 순으로 사자지면서 빵꾸가 난다.
    음식들이 자기 차례가 오는 순서는 idx+len(food_times)
    빵꾸가 날때 마다 자기 차례로 오는 시간이 줄어든다.
"""


def solution(food_times, k):
    sorted_time = sorted(food_times)
    cycle = len(food_times)
    end_time = 0
    prev_food = 0
    prev_end_time = 0
    for i in range(len(sorted_time)):
        food = sorted_time[i]
        if food == prev_food:
            cycle -= 1
        else:
            prev_end_time = end_time
            end_time += (food - prev_food) * cycle
            if end_time > k:
                break
            prev_food = food
            cycle -= 1
    else:
        return -1

    time = prev_end_time + (k - prev_end_time) // cycle * cycle
    for i in range(len(food_times)):
        if food_times[i] < food:
            continue
        if time == k:
            return i + 1
        else:
            time += 1


print(solution([3, 1, 1, 2], 6))
