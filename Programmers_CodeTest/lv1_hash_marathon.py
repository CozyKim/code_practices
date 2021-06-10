def solution(participant, completion):
    answer = ''
    names = {}
    for person in participant:
        if person in names:
            names[person] += 1
        else:
            names[person] = 1

    for person in completion:
        if person in names:
            names[person] -= 1
    answer += [n for n, N in names.items() if N == 1][0]
    return answer


solution(["leo", "kiki", "eden"], ["eden", "kiki"])
