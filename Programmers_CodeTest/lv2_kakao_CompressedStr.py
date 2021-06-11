

def solution(s: str):
    answer = []
    slider = [i for i in range(1, len(s)+1)]
    last = ''
    _s = []
    sldrs = []
    flag = 0
    tmp = ''
    for sldr in slider:
        sldrs.append([i for i in range(1, len(s)+1) if i % sldr == 0])
        if sldrs[-1][-1] != len(s):
            sldrs[-1].append(len(s))
    print(sldrs)
    for splts in sldrs:
        while splts:
            idx_end = splts.pop()
            if len(splts) != 0:
                idx_start = splts[-1]
            else:
                idx_start = 0
            _s.insert(0, s[idx_start:idx_end])
        print(_s)
        cnt = 1
        for idx, alpha in enumerate(_s):
            if idx == len(_s)-1:
                if alpha == last:
                    cnt += 1
                    tmp += str(cnt) + alpha
                else:
                    if flag:
                        tmp += str(cnt)+last+alpha
                    else:
                        tmp += last+alpha
                cnt = 1
                flag = 0
            else:
                if alpha == last:
                    cnt += 1
                    flag = 1
                else:
                    if flag:
                        tmp += str(cnt)+last
                        flag = 0
                    # elif len(_s) == len(s):
                    else:
                        tmp += last
                    cnt = 1
                last = alpha
        print(tmp)
        answer.append(len(tmp) if len(tmp) != 0 else len(s))
        _s = []
        tmp = ''
        last = ''
    print(answer)
    return min(answer)


solution('aabbaccc')
