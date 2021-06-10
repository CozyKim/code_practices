def solution(numbers, hand):
    answer = ''
    _star = 77  # '*'
    _shop = 99  # '#'
    L_position = 77  # '*'
    R_position = 99  # '#'
    keypad = {_star: [0, 0], 0: [1, 0], _shop: [2, 0],
              7: [0, 1], 8: [1, 1], 9: [2, 1],
              4: [0, 2], 5: [1, 2], 6: [2, 2],
              1: [0, 3], 2: [1, 3], 3: [2, 3]}
    for num in numbers:
        if num == 1 or num == 4 or num == 7:    # L
            L_position = num
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:  # R
            R_position = num
            answer += 'R'
        else:
            L_cnt = distance(L_position, num, keypad)
            R_cnt = distance(R_position, num, keypad)
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


def distance(start, goal, keypad: dict):
    return sum([abs(a-b) for a, b in zip(keypad[start], keypad[goal])])
