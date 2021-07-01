# https://programmers.co.kr/learn/courses/30/lessons/17676

from collections import deque


def solution(lines):
    answer = 0

    starts = []
    ends = []

    for line in lines:
        start, end = pre_processing(line)
        starts.append(start)
        ends.append(end)
    starts.sort()
    ends.sort()

    checktimes = deque(sorted(starts+ends))
    tmp = 0
    while checktimes:
        add = 0
        sub = 0
        time = checktimes.popleft()
        for i in starts:
            if i < time + 1:
                add += 1
            else:
                break
        starts = starts[add:]
        for i in ends:
            if i < time:
                sub += 1
            else:
                break
        ends = ends[sub:]
        tmp += add - sub
        answer = max(answer, tmp)
    print(answer)
    return answer


def pre_processing(line: str):
    day, time, processed_time = line.split()
    h, m, s = time.split(':')
    s = float(h) * 3600 + float(m) * 60 + float(s)
    start_time, end_time = round(
        s - float(processed_time[:-1]) + float(0.001), 3), s
    return [start_time, end_time]


solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
         )
