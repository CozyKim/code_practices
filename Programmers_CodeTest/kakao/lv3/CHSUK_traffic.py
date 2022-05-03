# https://programmers.co.kr/learn/courses/30/lessons/17676


def time_to_sec(string):
    h, m, s = string.split(":")
    return int((int(h) * 3600 + int(m) * 60 + float(s)) * 1000)


def solution(lines):
    answer = 0
    end_times = [time_to_sec(line.split()[1]) for line in lines]
    start_times = [
        end_times[i] - int(float(lines[i].split()[2][:-1]) * 1000) + 1
        for i in range(len(lines))
    ]
    end_times.sort()
    start_times.sort()
    s_idx, e_idx = 0, 0
    for time in sorted(start_times + end_times):
        if time < 0:
            continue
        while s_idx < len(start_times) and start_times[s_idx] < time + 1000:
            s_idx += 1
        while e_idx < len(end_times) and end_times[e_idx] < time:
            e_idx += 1
        answer = max(answer, s_idx - e_idx)
    return answer


solution(
    [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s",
    ]
)
