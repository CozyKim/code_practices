# https://programmers.co.kr/learn/courses/30/lessons/17684


def solution(msg):
    answer = []
    dictionary = {}
    next_index_num = 1
    # init
    for i in range(ord("A"), ord("Z") + 1):
        dictionary[chr(i)] = i - ord("A") + 1
        next_index_num += 1
    i = 0
    j = 1
    while i < len(msg):
        while j < len(msg) and msg[i : j + 1] in dictionary:
            j += 1
        if msg[i : j + 1] not in dictionary:
            dictionary[msg[i : j + 1]] = next_index_num
            next_index_num += 1
        answer.append(dictionary[msg[i:j]])
        i = j
        j += 1

    return answer


solution("KAKAO")
solution("TOBEORNOTTOBEORTOBEORNOT")
solution("A")
