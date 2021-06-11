def solution(record: list):
    answer = []
    users = {}
    tmp = []
    record = [s.split() for s in record]
    print(record)
    for R in record:
        if 3 == len(R):
            op, user, name = R
            if op == 'Enter':
                users[user] = name
                tmp.append([op, user])
            elif op == 'Change':
                users[user] = name
        else:
            op, user = R
            tmp.append([op, user])
    for op, user in tmp:
        if op == 'Enter':
            answer.append(users[user]+'님이 들어왔습니다.')
        else:
            answer.append(users[user]+'님이 나갔습니다.')
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
         "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
