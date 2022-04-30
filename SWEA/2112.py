# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu

"""
통과 조건
    세로가 A나 B 로 K 만큼 연속으로 있을 때 그 줄은 통과
    모든 세로줄이 통과 해야 성공
약품
    가로 줄에 약품 A나 B를 넣으면 그 줄은 모두 약품의 특성으로 바뀐다
    이는 최소한 쓰는 것이 좋다

"""


def check_film(chemical):
    global W, D, K, film_info
    for c in range(W):
        cnt = 1
        prev = chemical[0] if chemical[0] != -1 else film_info[0][c]
        for r in range(1, D):
            if r + K - cnt > D:
                return False
            cur = chemical[r] if chemical[r] != -1 else film_info[r][c]
            cnt = cnt + 1 if cur == prev else 1
            if cnt == K:
                break
            prev = cur
        else:
            return False
    return True


def dfs(col, chemical, cnt):
    global answer
    if answer <= cnt:
        return
    if check_film(chemical):
        answer = min(answer, cnt)
        return
    for i in range(col + 1, D + 1):
        chemical[col] = 0
        dfs(i, chemical, cnt + 1)
        chemical[col] = 1
        dfs(i, chemical, cnt + 1)
        chemical[col] = -1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    D, W, K = map(int, input().split())
    film_info = [list(map(int, input().split())) for _ in range(D)]
    if K == 1:
        print(f"#{test_case} 0")
        continue
    answer = float("inf")
    CHEMICAL = [-1] * D
    for i in range(D):
        dfs(i, CHEMICAL, 0)
    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
