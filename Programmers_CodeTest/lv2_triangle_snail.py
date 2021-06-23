
# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    case = [[None]*i for i in range(1, n+1)]
    print(case)
    # 움직임은 아래 -> 오른쪽 -> 위(대각선위) 를 반복
    x, y = -1, 0
    num = 1
    for direct in range(n):
        for i in range(direct, n):
            if direct % 3 == 0:
                x += 1
            elif direct % 3 == 1:
                y += 1
            elif direct % 3 == 2:
                x -= 1
                y -= 1
            case[x][y] = num
            num += 1

    for i in case:
        answer += i
    print(answer)
    return answer


solution(4)
