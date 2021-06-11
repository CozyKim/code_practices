from collections import deque


def solution(s):
    token_s = deque([i for i in s])
    check = deque([token_s.popleft()])
    while token_s:
        if len(check):
            if check[-1] == token_s[0]:
                check.pop()
                token_s.popleft()
            else:
                check.append(token_s.popleft())
        else:
            check.append(token_s.popleft())
    return 1 if len(check) == 0 else 0


print(solution('cdcd'))
