# https://programmers.co.kr/learn/courses/30/lessons/17682

import re


def solution(dartResult):
    answer = []
    scores = re.findall("[\d]+", dartResult)
    results = re.findall("([SDT])([*#]*)", dartResult)
    option = {"": 1, "*": 2, "#": -1}
    bonus = {"S": 1, "D": 2, "T": 3}
    for i in range(3):
        if results[i][1] == "*" and i > 0:
            answer[i - 1] *= 2
        answer.append(int(scores[i]) ** bonus[results[i][0]] * option[results[i][1]])
    print(answer)
    return sum(answer)


solution("1S2D*3T")
