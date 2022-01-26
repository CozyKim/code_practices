# https://www.acmicpc.net/problem/1476

"""
문제 설명
    준규가 사는 나라에는 3개를 이용하여 연도를 나타낸다.
    각각 수는 지구, 태양, 달을 나타낸다.
    우리가 알고 있는 1년은 준규가 살고있는 나라에서는 1 1 1 로 나타낼 수 있다.
    1년이 지날 때 마다, 세 수는 모두 1씩 증가
    만약, 어떤 수가 범위를 넘어가는 겨웅에는 1이된다.
    각각의 범위는 1~15, 1~28, 1~!9

입력 
    첫째 줄에 세수 E, S, M 이 주어진다.

출력 
    E,S,M이 표현해주는 연도 중에서 가장 빠른 연도 
"""


def main():
    E, S, M = map(int, input().split())
    E -= 1
    S -= 1
    M -= 1
    # 풀이 1

    # 모두가 서로소이다. -> S를 기준으로 키워간다. 그러다 둘 중 하나와 겹치게 된다면 그 시점부터 둘의 최소 공배수를 기준으로 커진다. (계속 나머지 확인)

    # 가장 먼저 바로 조건에 해당하는지 확인
    e_mod = S % 15
    m_mod = S % 19
    if e_mod == M:
        if m_mod == E:
            print(S)
            return S + 1

    # 예측 값을 올려보자
    step = 28
    while m_mod != M or e_mod != E:
        # S 증가
        S += step

        # 나머지 재조정
        e_mod = S % 15
        m_mod = S % 19

        # 하나가 겹친다면 그 이후부터는 step 조정
        if m_mod == M:
            step = 28 * 19
        if e_mod == E:
            step = 28 * 15
    print(S + 1)
    return S + 1


if __name__ == "__main__":
    main()
