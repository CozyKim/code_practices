# https://programmers.co.kr/learn/courses/30/lessons/60058

"""
문제 설명 다른 개발자가 작성한 소스코드 분석하여 문제점 수정하라
대부분 소스코드 내 작성된 괄호가 개수는 밪지만 짝이 맞지 않은 형태로 작성
소스코드에 작성된 모든 괄호를 뽑아 올바른 순서로 배치된 괄호 문자열을 알려주는 프로그램을 개발 하려한다.

균형잡힌 괄호 문자열 : (와 )로만 이뤄진 문자열이 있을 경우 각각의 개수가 같을 경우
올바른 괄호 문자열 : () 균형에서 괄호의 짝도 맏을 경우

균형잡힌 -> 올바른 으로 바꾸는 방법 :
    1. 입력이 빈문자열인 경우 빈문자열 반환
    2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리 u는 균형 잡힌 괄호 문자열로 더이상 분리 할 수 없어야함 v는 빈 문자열이 될 수 있음
    3. 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계 부터 다시 수행
        3-1. 수행한 결과를 u에 이어 붙인 후 반환
    4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
        4-1. 빈 문자열에 첫 번째 문자로 '('를 붙인다
        4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
        4-3. ')' 를 다시 붙인다.
        4-4. u의 첫 번쨰와 마지막 문자를 제거, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
        4-5. 생성된 문자열 반환
"""

p = "()))((()"


def balance_string(string):
    left_cnt, right_cnt = 0, 0
    for i in range(len(string)):

        if string[i] == "(":
            left_cnt += 1
        else:
            right_cnt += 1
        if left_cnt and left_cnt == right_cnt:
            return string[: i + 1], string[i + 1 :]


def right_string(string):
    cnt = 0
    for i in range(len(string)):
        if string[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True


def solution(p):
    if not p:
        return p
    mapping = {"(": ")", ")": "("}
    u, v = balance_string(p)
    if right_string(u):
        return u + solution(v)
    else:
        tmp = "("
        tmp += solution(v) + ")"
        return tmp + "".join([mapping[i] for i in u[1:-1]])


solution(p)
