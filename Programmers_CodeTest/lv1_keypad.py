# def solution(numbers, hand):
#     answer = ''
#     L_position = 77 # '*'
#     R_position = 99 # '#'
#     for num in numbers:

#     return answer

from typing import Dict


def solution(numbers, hand):
    answer = ''
    _star = 77  # '*'
    _shop = 99  # '#'
    L_position = 77  # '*'
    R_position = 99  # '#'
    root_L = {_star: [7, 0], 7: [4, 8], 4: [1, 5, 7], 1: [
        2, 4], 2: [1, 5], 5: [2, 4, 8], 8: [5, 7, 0], 0: [8]}
    root_R = {_shop: [9, 0], 9: [6, 8], 6: [3, 5, 9], 3: [
        2, 6], 2: [3, 5], 5: [2, 6, 8], 8: [5, 9, 0], 0: [8]}
    for num in numbers:
        if num == 1 or num == 4 or num == 7:    # L
            L_position = num
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:  # R
            R_position = num
            answer += 'R'
        else:
            L_cnt = bfs(L_position, num, root_L)
            R_cnt = bfs(R_position, num, root_R)
            if L_cnt > R_cnt:
                R_position = num
                answer += 'R'
            elif L_cnt < R_cnt:
                L_position = num
                answer += 'L'
            else:
                if hand == 'left':
                    L_position = num
                    answer += 'L'
                else:
                    R_position = num
                    answer += 'R'
    return answer


def bfs(num, goal, root: dict):
    visited = [num]
    que = [num]
    cnt = 0
    last_num = num
    if num == goal:
        return 0
    while que:
        num = que.pop(0)
        if num == root[last_num][0]:
            last_num = num
            cnt += 1
        for i in root[num]:
            if i == goal:
                return cnt + 1
            if i not in visited:
                visited.append(i)
                que.append(i)


root_R = {77: [9, 0], 9: [6, 8], 6: [3, 5, 9], 3: [
    2, 6], 2: [3, 5], 5: [2, 6, 8], 8: [5, 9, 0], 0: [8]}
bfs(6, 5, root_R)
print(solution([0, 8, 6, 8], "right"))
