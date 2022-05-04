# https://programmers.co.kr/learn/courses/30/lessons/60059
"""
문제 설명
    열쇠와 함께 자물쇠를 푸는 방법에 대해 적인 종이가 주어진다.
    자물쇠는 격자 한칸의 크기가 1x1인 NxN 크기의 정사각 격자 형태
    열쇠는 MxM 크기의 정사각 격자 형태로 되어있다.
    열쇠의 돌기 부분과 자물쇠의 홈 부분이 딱 맞게 채우면 자물쇠가 열리는 구조

조건
    자물쇠 영역을 벗어난 부분이 있는 열쇠의 홈과 돌기는 자물쇠여는데 영향 X
    자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치 해야함
    열쇠의 돌기와 자물쇠 돌기 만나선 안됨
    자물쇠의 모든 홈을 채워 비어있는 곳이 없어야함
"""


def rotate_90_keys(key):
    result = []
    for j in range(len(key)):
        tmp = []
        for i in range(len(key) - 1, -1, -1):
            tmp.append(key[i][j])
        result.append(tmp[:])
    return result


def find_axis(board):
    axis = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                axis.append((i, j))
    return axis


def make_rotated_keys(key):
    result, axis = [], []
    result.append(rotate_90_keys(key))
    for _ in range(3):
        result.append(rotate_90_keys(result[-1]))
    for board in result:
        axis.append(find_axis(board))
    return axis


def solution(key, lock):
    extend_lock = [
        [0] * (2 * len(key) + len(lock)) for _ in range(2 * len(key) + len(lock))
    ]
    blank_axis = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            extend_lock[i + len(key)][j + len(key)] = lock[i][j]
            if not lock[i][j]:
                blank_axis.append((i + len(key), j + len(key)))

    rotated_keys = make_rotated_keys(key)
    for i in range(len(key) + len(lock)):
        for j in range(len(key) + len(lock)):
            for axis in rotated_keys:
                cnt = 0
                for dr, dc in axis:
                    if extend_lock[i + dr][j + dc]:
                        break
                    elif len(key) <= i + dr < len(key) + len(lock) and len(
                        key
                    ) <= j + dc < len(key) + len(lock):
                        cnt += 1
                    if cnt == len(blank_axis):
                        return True
    return False


print(solution([[0, 0, 0], [0, 1, 0], [1, 0, 0]], [[1, 0, 1], [1, 1, 1], [1, 1, 1]]))
