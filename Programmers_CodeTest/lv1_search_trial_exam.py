def solution(answers):
    answers_len = len(answers)
    tep_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    tep_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    _1 = [i % 5+1 for i in range(answers_len)]
    _2 = [tep_2[i % 8] for i in range(answers_len)]
    _3 = [tep_3[i % 10] for i in range(answers_len)]
    for n in range(answers_len):
        if answers[n] != _1[n]:
            _1[n] = 0
        if answers[n] != _2[n]:
            _2[n] = 0
        if answers[n] != _3[n]:
            _3[n] = 0
    score_1 = answers_len - _1.count(0)
    score_2 = answers_len - _2.count(0)
    score_3 = answers_len - _3.count(0)
    scores = [score_1, score_2, score_3]

    answer = [i+1 for i, v in enumerate(scores) if v == max(scores)]
    return answer


print(solution([1, 3, 2, 4, 2]))
