# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3

def solution(n, times):
    answer = 0
    min_try = 1                 # 심사하는데 걸리는 시간이 가장 빠른 경우
    max_try = max(times) * n    # n 명을 심사하는데 걸리는 시간이 가장 느린 경우

    while min_try <= max_try:   # n 명을 심사할 수 있는 가장 빠른 시간(심사 인원 n명을 만족하는)을 찾아보자
        mid_try = (max_try + min_try) // 2  # 이분 탐색 시작
        cnt = 0
        for time in times:      # times에 있는 심사 시간을 기준으로 mid_try시간동안 몇명을 심사 할 수 있는지 확인
            cnt += mid_try // time
            if cnt >= n:
                break  # times 안에 n명 이상을 심사할 수 있으면 mid_try 보다 큰 시간들은 모두 심사 가능

        if cnt >= n:           # times 안에 n명 이상을 심사 할 수 있으므로 n명 심사하는데 걸리는 시간이 가장 느린 경우의 범위를 줄인다
            answer = mid_try
            max_try = mid_try - 1
        elif cnt < n:           # times 안에 n명 을 심사 할 수 없으므로 가장 빨리 끝나는 시간을 좀 더 높여 mid 를 오른쪽으로 이동시키자
            min_try = mid_try + 1

    return answer


solution(6, [7, 10])
solution(5, [3, 9])
solution(4, [1, 1])
solution(3, [1, 1])
