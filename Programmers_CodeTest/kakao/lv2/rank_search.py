# https://programmers.co.kr/learn/courses/30/lessons/72412
"""
지원서 작성시
1. 개발 언어 항목 : cpp, java, python
2. 직군 : backend, frontend
3. 경력구분 : junior, senior
4. 소울 푸드 : chicken, pizza
를 반드시 선택
개발팀에게 이를 분석해서 넘겨준다.

개발팀에서 궁금해하는 내용은
* [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?

input : 
    info(str) - 지원서에 입력한 4가지 정보 & 획득한 코딩테스트 점수
        "개발언어 직군 경력 소울푸드 점수"
    query(str) - 개발팀이 궁금해하는 문의조건
        "개발언어 and 직군 and 경력 and 소울푸드"
        '-' 표시는 해당 조건을 고려하지 않겠다는 의미
        X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미
output:
    answer(int) - 문의 조건에 만족하는 인원수
"""


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]  # * 5000
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]  # * 10000

import time


def solution(info, query):
    start = time.time()
    answer = []
    mapping = {}
    for idx, lang in enumerate(["cpp", "java", "python"]):
        for job in ["backend", "frontend"]:
            try:
                mapping[lang][job] = {}
            except:
                mapping[lang] = {job: {}}
            for career in ["junior", "senior"]:
                try:
                    mapping[lang][job][career] = {}
                except:
                    mapping[lang][job] = {career: {}}
                for food in ["chicken", "pizza"]:
                    try:
                        mapping[lang][job][career][food] = []
                    except:
                        mapping[lang][job][career] = {food: []}

    for info_ in info:
        lang, job, career, food, score = info_.split()
        mapping[lang][job][career][food].append(int(score))
    print(time.time() - start)
    # '-'를 확인해주는 함수

    def binary_search(list, q):
        if list[0] >= q:
            return -1
        if list[-1] < q:
            return len(list) - 1
        left, right = 0, len(list) - 1
        while right - left > 1:
            if list[(left + right) // 2] < q:
                left = (left + right) // 2
            else:
                right = (left + right) // 2
        return left

    def check_dash(lst: list):
        # lang = '-' 경우
        result = []
        result.append(["cpp", "java", "python"]) if lst[0] == "-" else result.append(
            [lst[0]]
        )
        result.append(["backend", "frontend"]) if lst[2] == "-" else result.append(
            [lst[2]]
        )
        result.append(["junior", "senior"]) if lst[4] == "-" else result.append(
            [lst[4]]
        )
        result.append(["chicken", "pizza"]) if lst[6] == "-" else result.append(
            [lst[6]]
        )
        return result

    tmp = 0
    for query_ in query:
        lang, _, job, _, career, _, food, score = query_.split()
        lang, job, career, food = check_dash([lang, _, job, _, career, _, food])
        cnt = 0
        for l in lang:
            for j in job:
                for c in career:
                    for f in food:
                        if mapping[l][j][c][f]:
                            tmp1 = time.time()
                            # for s in mapping[l][j][c][f]:
                            #     if s >= int(score):
                            #         cnt += 1
                            t = sorted(mapping[l][j][c][f])
                            cnt += len(t) - (binary_search(t, int(score)) + 1)

                            tmp += time.time() - tmp1
        answer.append(cnt)
    print(tmp)
    print(time.time() - start)
    return answer


# print(solution(info, query))
# solution(info, query)


def solution(info, query):
    start = time.time()
    answer = []
    mapping = {}
    for idx, lang in enumerate(["cpp", "java", "python", "-"]):
        for job in ["backend", "frontend", "-"]:
            try:
                mapping[lang][job] = {}
            except:
                mapping[lang] = {job: {}}
            for career in ["junior", "senior", "-"]:
                try:
                    mapping[lang][job][career] = {}
                except:
                    mapping[lang][job] = {career: {}}
                for food in ["chicken", "pizza", "-"]:
                    try:
                        mapping[lang][job][career][food] = []
                    except:
                        mapping[lang][job][career] = {food: []}

    for info_ in info:
        lang, job, career, food, score = info_.split()
        # mapping[lang][job][career][food].append(score)
        for l in [lang, "-"]:
            for j in [job, "-"]:
                for c in [career, "-"]:
                    for f in [food, "-"]:
                        mapping[l][j][c][f].append(int(score))
    print(time.time() - start)
    # return mapping
    # '-'를 확인해주는 함수
    def binary_search(list, q):
        if list[0] >= q:
            return -1
        if list[-1] < q:
            return len(list) - 1
        left, right = 0, len(list) - 1
        while right - left > 1:
            if list[(left + right) // 2] < q:
                left = (left + right) // 2
            else:
                right = (left + right) // 2
        return left

    tmp = 0
    for idx, lang in enumerate(["cpp", "java", "python", "-"]):
        for job in ["backend", "frontend", "-"]:
            for career in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    tmp1 = time.time()
                    mapping[lang][job][career][food].sort()
                    tmp += time.time() - tmp1
    print(tmp)

    tmp = 0
    for query_ in query:
        lang, _, job, _, career, _, food, score = query_.split()
        cnt = 0
        tmp1 = time.time()
        if mapping[lang][job][career][food]:
            cnt = len(mapping[lang][job][career][food]) - (
                binary_search(mapping[lang][job][career][food], int(score)) + 1
            )
        # for s in mapping[lang][job][career][food]:
        #     if s >= int(score):
        #         cnt += 1
        tmp += time.time() - tmp1
        answer.append(cnt)
    print(tmp)
    print(time.time() - start)
    return answer


print(solution(info, query))
# solution(info, query)
