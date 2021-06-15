

def solution(numbers):
    answer = ''
    _numbers = {}
    tmp3 = []
    a = list(map(str, numbers))

    for i in a:
        if i[0] not in _numbers:
            _numbers[i[0]] = [i]
        else:
            _numbers[i[0]].append(i)

    for n in _numbers:
        n_numbers = _numbers[n]
        tmp = []
        for i in n_numbers:
            tmp.append([i + n*(3-len(i)), i])
        tmp.sort()
        tmp2 = [tmp.pop()[1]]
        while tmp:
            extend_num, num = tmp.pop()
            if len(tmp) != 0:
                if tmp2[-1] == extend_num:
                    if extend_num[0] < extend_num[1]:
                        tmp2.insert(tmp2.index(tmp2[-1]), num)
                    else:
                        tmp2.append(num)
                else:
                    tmp2.append(num)
            else:
                tmp2.append(num)
            print(tmp2)
        tmp3.append(''.join(tmp2))
        print(tmp3)
    tmp3.sort(reverse=True)
    print(tmp3)
    print(''.join(tmp3))
    return ''.join(tmp3)


solution([1, 0, 1, 11, 131, 1000, 2, 242, 212, 21, 24,
         42, 220, 221, 222, 223, 234, 234, 224, 0, 0])
