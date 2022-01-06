"""
문제 설명
    셔틀은 09:00 부터 총 n회 t분 간격으로 역에 도착, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
    도착한 순간 대기열에서 선 크루까지 포함해 대기 순서대로 태우고 바로 출발
    셔틀을 타고 사무실에 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라
조건
    09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.
    같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다. 또한 모든 크루는 잠을 자야함 23:59에 딥에 돌아간다.
    따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.

입력 형식
    n : 셔틀 운행 횟수
    t : 셔틀 운행 간격
    m : 한 셔틀에 탈 수 있는 최대 크루 수 
    timetable : 크루가 대이열에 도착하는 시각을 모은 배열
"""

# 목표 : 가장 마지막 셔틀 버스에 타자 !
# 조건 : 만약 같은시간에 와서 짤릴 경우 그 짤리는 시간 보다 1분 일찍 오자

# 경우1 : 기다리는 사람 다 탔는데 아직 자리와 셔틀이 남았을 경우
# 경우2 : 기다리는 사람 다 안 탔는데 짤릴 경우

# 현재 시간 + 셔틀 시간 간격 값을 HH:MM으로 바꿔주는 함수

# HH:MM -> 숫자로 바꿔주는 함수
from collections import deque


def HHMM_to_minute(time: str) -> int:
    time = time.split(":")
    return 60 * int(time[0]) + int(time[1])


def minute_to_HHMM(time: int) -> str:
    h, m = divmod(time, 60)
    return "{:0>2}:{:0>2}".format(h, m)


def solution(n, t, m, timetable):
    answer = ""

    # 타임 테이블을 분으로 바꾸기
    timetable_minute = []
    for time in timetable:
        timetable_minute.append(HHMM_to_minute(time))

    # 타임 테이블 정렬
    timetable_minute.sort()
    timetable_minute = deque(timetable_minute)
    # 현재 시간 <- 현재 시간 + 운행 간격 시간
    present_time = HHMM_to_minute("09:00")
    LAST = False
    for i in range(n):
        if i == n - 1:
            LAST = True
        riding_num = 0
        last_time = present_time
        while timetable_minute and riding_num < m:
            time = timetable_minute.popleft()
            if time > present_time:
                timetable_minute.appendleft(time)
                break
            last_time = time
            riding_num += 1
        if LAST:
            if riding_num < m:
                answer = present_time
            else:
                # if timetable_minute:
                #     if last_time == timetable_minute[0]:
                answer = last_time - 1
        present_time += t

    print(minute_to_HHMM(answer))
    return minute_to_HHMM(answer)


solution(
    10,
    60,
    45,
    [
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
    ],
)
