def solution(s):
    answer = []
    zeronum = 0
    cnt = 0
    while s != '1':
        if '0' in s:
            zeronum += s.count('0')
            s = s.replace('0', '')
        n = len(s)
        s = bin(n)[2:]
        cnt += 1
    answer = [cnt, zeronum]
    return answer


solution("110010101001"	)
