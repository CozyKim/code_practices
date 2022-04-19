def solution(play_time, adv_time, logs):
    answer = 0

    def time_to_sec(origin: str) -> int:
        h, m, s = map(int, origin.split(":"))
        return 3600 * h + m * 60 + s

    def time_to_origin(sec: int) -> str:
        h, left = divmod(sec, 3600)
        m, s = divmod(left, 60)
        return h, m, s

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    play_list = [0] * (play_time_sec + 1)
    for log in logs:
        s, e = log.split("-")
        s, e = time_to_sec(s), time_to_sec(e)
        play_list[s] += 1
        play_list[e] -= 1
    n = 0

    # 누적합으로 가장 많이 겹치는 부분 구하기
    for i in range(len(play_list)):
        n += play_list[i]
        play_list[i] = n

    tmp = max_time = sum(play_list[:adv_time_sec])

    for i in range(len(play_list) - adv_time_sec):
        tmp += -play_list[i] + play_list[i + adv_time_sec]
        if tmp > max_time:
            answer = i + 1
            max_time = tmp
    h, m, s = time_to_origin(answer)
    answer = "{:0>2}:{:0>2}:{:0>2}".format(h, m, s)
    return answer


solution(
    "02:03:55",
    "00:14:15",
    [
        "01:20:15-01:45:14",
        "00:25:50-00:48:29",
        "00:40:31-01:00:00",
        "01:37:44-02:02:30",
        "01:30:59-01:53:29",
    ],
)
solution(
    "99:59:59",
    "25:00:00",
    [
        "69:59:59-89:59:59",
        "01:00:00-21:00:00",
        "79:59:59-99:59:59",
        "11:00:00-31:00:00",
    ],
)
