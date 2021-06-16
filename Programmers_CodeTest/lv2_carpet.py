def solution(brown, yellow):
    answer = []
    brown_N_yellow = brown+yellow
    lists = []
    for i in range(3, brown_N_yellow//2+1):
        if brown_N_yellow % i == 0:
            sub = sorted([brown_N_yellow//i, i], reverse=True)
            if sub not in lists:
                lists += [sub]
    for x, y in lists:
        if (x-2) * (y-2) == yellow:
            answer = [x, y]
            break
    # print(answer)
    return answer


solution(10, 2)
