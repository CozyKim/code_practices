def solution(n, arr1, arr2):
    answer = []
    tmp = ''
    for a, b in zip(arr1, arr2):
        for i, j in zip(dec_to_bin(n, a), dec_to_bin(n, b)):
            if int(i) or int(j):
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
        tmp = ''
    return answer


def dec_to_bin(n, arr):
    tmp = ''
    for i in range(n-1, -1, -1):
        tmp += str(arr // (2**i))
        arr = arr % (2**i)
    return tmp


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
