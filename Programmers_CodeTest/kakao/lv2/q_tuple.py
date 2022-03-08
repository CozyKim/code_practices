# https://programmers.co.kr/learn/courses/30/lessons/64065


def solution(s):
    answer = []

    def str_to_set(str: str):
        str = str[1:-1]
        sets = []
        for idx, s in enumerate(str):
            if s == "{":
                s_point = idx + 1
            elif s == "}":
                sets.append(set(str[s_point:idx].split(",")))
        return sorted(sets, key=len)

    sets = str_to_set(s)

    last_set = set([])
    for subset in sets:
        answer.append(int(*list(subset - last_set)))
        last_set = subset
    print(answer)
    return answer


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
