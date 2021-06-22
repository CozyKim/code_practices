# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number: str, k):
    global answer
    answer = ''

    for i in '9876543210':
        if i in number:
            if number.index(i) <= k:
                k -= number.index(i)
                number = number[number.index(i):]
                break

    def opt(answers, k, last):
        global answer
        if k == 0:
            answer += answers
            return
        for idx, i in enumerate(answers):
            if last < i:
                answers = answers[:idx-1]+answers[idx:]
                opt(answers, k - 1, answers[0])
                return
            if idx == len(answers) - 1 and k != 0:
                answer += answers[:idx+1 - k]
                return
            last = i
    opt(number, k, number[0])

    print(answer)
    return answer


solution("1119"	, 3)
