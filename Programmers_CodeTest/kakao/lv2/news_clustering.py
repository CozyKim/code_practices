# https://programmers.co.kr/learn/courses/30/lessons/17677
"""
문제 설명
    유사한 기사를 묶는 것을 하고 싶다
    논문과 자료조사를 통해 자카드 유사도라는 방법을 찾았다.
    문자열 사이의 유사도를 구하는데 무자열을 두 글자씩 끊어서 다중집합을 만들 수 있다.

자카드 유사도
    두 집합의 교집합 크기를 두집합의 합집합 크기로 나눈 값
    모두가 공집합일 경우에는 나눗셈이 정의되지 않으니 1로 정의
    원소의 중복을 허용하는 다중집합에서도 사용할 수 있다. 
        예를 들어 A는 원소 1을 3개 가지고 있고 B는 원소 1을 5개 가지고 있다할 때
        교집합은 min(3,5) 합집합은 max(3,5)가 된다.

조건
    입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
    입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 
    이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 
    예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
    다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.

"""

import re
from collections import defaultdict


def solution(str1: str, str2: str):
    answer = 0
    # 모두 소문자로 만들기
    str1 = str1.lower()
    str2 = str2.lower()

    print(str1)
    print(str2)

    # 두 글자씩 끊어서 dict에 넣기
    # 그리고 끊은 것 중에 영어가 아닌 것들은 버리기
    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)

    for i in range(len(str1) - 1):
        if re.search("[^(a-z)]", str1[i : i + 2]):
            continue
        str1_dict[str1[i : i + 2]] += 1
    for i in range(len(str2) - 1):
        if re.search("[^(a-z)]", str2[i : i + 2]):
            continue
        str2_dict[str2[i : i + 2]] += 1
    print(str1_dict)
    print(str2_dict)

    # 조건 : 둘 다 공집합일 경우
    if not str1_dict and not str2_dict:
        return 1 * 65536

    # set을 통해 집합계산 하기
    str1_set = set(str1_dict.keys())
    str2_set = set(str2_dict.keys())
    print(str1_set)
    print(str2_set)
    product_set = str1_set and str2_set
    sum_set = str1_set | str2_set

    # 계산 할 때, 다중 집합일 수 있으니 min, max 조건 추가하기
    prod = 0
    sums = 0
    for s in product_set:
        prod += min(str1_dict[s], str2_dict[s])
    for s in sum_set:
        sums += max(str1_dict[s], str2_dict[s])

    # 최종 답에 65536 곱하기
    answer = int(prod / sums * 65536)
    return answer


# sol = solution("FRANCE", "french")
sol = solution("handshake", "shake hands")
