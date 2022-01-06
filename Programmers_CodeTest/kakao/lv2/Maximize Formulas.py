# https://programmers.co.kr/learn/courses/30/lessons/67257
"""
문제 설명
    숫자들과 3가지의 연산 문자만으로 이루어진 연산 수식 전달
    연산자의 우선순위 자유롭게 재정의 후 가장 큰 숫자 제출

조건
    연산자의 우선순위 새로 정의 시, 같은 순위의 연산자는 없어야함
    만약 계산된 결과가 음수라면 절댓값으로 반환하여 제출
    expression은 공백, 괄호 없이 오로지 숫자와 3가지 연산자(+,-,*) 만으로 이루어짐
    옳바른 연산만 입력으로 주어짐
    0<= 피연산자 <1000
    같은 연산자 끼리는 앞에 있는 것의 우선순위가 더 높다
"""

expression = "100-200*300-500+20"
# expression = "50*6-3*2"

from itertools import permutations
import re


def solution(expression: str):
    answer = -1
    # 연산 순위 재정의 -> 총 6가지의 경우의 수
    # 순열 계산
    priority = list(permutations(["+", "-", "*"], 3))
    print(priority)
    # 각 연산자를 기준으로 자르고 eval 계산
    for steps in priority:
        test_expression = expression
        print(steps)
        print(test_expression)
        minus = False
        for step in steps:
            tmp_cal = 1
            while tmp_cal:
                if minus:
                    tmp_cal = re.findall(f"-?[0-9]+\{step}-?[0-9]+", test_expression)
                else:
                    if step == "-":
                        minus = True
                    tmp_cal = re.findall(f"[0-9]+\{step}[0-9]+", test_expression)
                print(tmp_cal)
                if tmp_cal:
                    i = tmp_cal[0]
                    tmp_i = i.replace(step, "\\" + step)
                    test_expression = re.sub(tmp_i, str(eval(i)), test_expression)
                print(test_expression)
        # 각 계산 한 것을 값 비교
        if re.search(f"-?[0-9]+\{step}-?[0-9]+", test_expression):
            continue
        answer = max(answer, abs(eval(test_expression)))
        print(answer)
    # 계산 결과는 절대값

    return answer


solution(expression)
