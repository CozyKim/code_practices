def solution(new_id: str):
    answer = ''
    last_s = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for s in new_id:
        if s in 'abcdefghijfklmnopqrstuvwxyz0123456789-_.':
            answer += s
    new_id = answer[:]
    answer = ''

    # 3단계
    for s in new_id:
        if last_s == '.' and s == '.':
            continue
        else:
            answer += s
        last_s = s
    new_id = answer[:]
    answer = ''

    # 4단계
    try:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    except:
        pass

    # 5단계
    if new_id == '':
        new_id = 'a'

    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


print(solution("abcdefghijklmn.p"))
