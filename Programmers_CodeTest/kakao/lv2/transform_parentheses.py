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

from collections import Counter, defaultdict


def solution(p):
    answer = ""

    # 균형잡힌 문자열 체크
    def balanced_check(str):
        cnts = Counter(str)
        if cnts["("] == cnts[")"]:
            return True
        return False

    # 올바른 문자열 체크
    def right_check(str):
        if not balanced_check(str):
            return False

        buckect = defaultdict(int)
        for s in str:
            if s == "(":
                buckect[s] += 1
            elif s == ")":
                if buckect["("] < buckect[")"] + 1:
                    return False
                buckect[s] += 1
        return True

    def inv_str(str):
        inv_dict = {"(": ")", ")": "("}
        result = ""
        for s in str:
            result += inv_dict[s]
        return result

    def func1(str: str):
        if not len(str):
            return ""

    def func2(str: str):
        for i in range(2, len(str) + 2, 2):
            u, w = str[:i], str[i:]
            if balanced_check(u) and balanced_check(w):
                return u, w

    def dfs(u):
        if func1(u) == "":
            return ""
        nw_u, nw_w = func2(u)

        if right_check(nw_u):
            return nw_u + dfs(nw_w)
            # return u + nw_u, w
        else:
            nw_w = dfs(nw_w)
            return "(" + nw_w + ")" + inv_str(nw_u[1:-1])

    answer = dfs(p)
    print(answer)
    return answer


solution(p)
