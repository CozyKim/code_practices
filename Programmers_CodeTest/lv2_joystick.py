# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def solution(name):
    answer = 0
    change = []
    tmp = []
    for s in name:
        if s == "A":
            change.append(0)
        else:
            change.append(1)

    def dfs(position, change, cnt=0):
        if sum(change) == 0:
            tmp.append(cnt)
            return
        change[position] = 0
        cnt += changing_cnt(name[position])
        if sum(change) == 0:
            tmp.append(cnt)
            return

        R_cnt = R_position = L_position = L_cnt = 0

        for i in range(position+1, len(name)+position):
            if change[i % len(name)] == 1:
                R_position = i % len(name)
                R_cnt = i-position
                break
        for i in range(position - 1, position - len(name), -1):
            if i < 0:
                i += len(name)
            if change[i] == 1:
                L_position = i
                L_cnt = position - \
                    i if i < position else len(name) - i + position
                break
        if R_cnt == 0:
            return
        _change = change[:]
        dfs(L_position, change, cnt + L_cnt)
        dfs(R_position, _change, cnt + R_cnt)

    dfs(0, change)
    print(tmp)
    return answer


def changing_cnt(target, start='A'):
    return ord('Z') - ord(target) + 1 if ord(target) - ord(start) > ord('Z') - ord(target) + 1 else ord(target) - ord(start)


solution("JAN")
