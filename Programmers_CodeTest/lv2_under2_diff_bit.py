# https://programmers.co.kr/learn/courses/30/lessons/77885?language=python3
def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = bin(num)[2:]
        if '0' in bin_num:
            n = bin_num[::-1].index('0')
            if n == 0:
                answer.append(num + 1)
            else:
                answer.append(num + 2 ** (n - 1))

        else:
            answer.append(num + 2 ** (len(bin_num) - 1))
    return answer
