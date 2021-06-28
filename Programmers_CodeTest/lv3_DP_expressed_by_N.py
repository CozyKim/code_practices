# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3

def solution(N, number):
    answer = -1
    dp = []
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    numbers.add(op1 - op2)
                    numbers.add(op1 + op2)
                    numbers.add(op1 * op2)
                    if op2 != 0:
                        numbers.add(op1 // op2)

        if number in numbers:
            answer = i
            break

        dp.append(numbers)

    return answer

# 핵심 : dp의 기준을 횟수에 초점
