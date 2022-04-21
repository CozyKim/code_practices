# https://programmers.co.kr/learn/courses/30/lessons/42893

import re


def solution(word, pages):
    answer = 0
    word = word.lower()
    pages_info = {}  # key : 웹 주소, value : 기본점수(int), 외부링크(list), url에 해당하는 index(int)

    def cnt_word(word, html):
        tmp = re.split("[^a-z]", html)
        return tmp.count(word)

    def find_url(text):
        check = re.compile(r"\"https://[^\"]+\"")
        tmp = check.findall(text)
        return list(map(lambda x: x[1:-1], tmp))

    def find_external_link(text):
        check = re.compile(r"<a href=\"https://[^\"]+\">")
        tmp = check.findall(text)
        result = []
        for t in map(lambda x: x[1:-1], tmp):
            result += find_url(t)
        return result

    def find_page_url(text):
        check = re.compile(r"<meta property=[^\>]+>")
        tmp = check.search(text)
        return find_url(tmp.group())

    for idx, page in enumerate(pages):
        page = page.lower()
        url = find_page_url(page)[0]
        pages_info[url] = {
            "score": cnt_word(word, page),
            "external_links": find_external_link(page),
            "index": idx,
        }

    scores = [0] * len(pages)
    ex_score = [0] * len(pages)

    for url in pages_info:
        for ex_page in pages_info[url]["external_links"]:
            if ex_page in pages_info:
                ex_score[pages_info[ex_page]["index"]] += pages_info[url][
                    "score"
                ] / len(pages_info[url]["external_links"])

    for url in pages_info:
        scores[pages_info[url]["index"]] = (
            pages_info[url]["score"] + ex_score[pages_info[url]["index"]]
        )

    result = 0

    for i in range(len(scores)):
        if scores[i] > answer:
            result = i
            answer = scores[i]

    return result


solution(
    "blind",
    [
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://a.com"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href="https://b.com"> Link to b </a>\n</body>\n</html>',
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://b.com"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href="https://a.com"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href="https://c.com"> Link to c </a>\n</body>\n</html>',
        '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://c.com"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href="https://a.com"> Link to a </a>\n</body>\n</html>',
    ],
)
