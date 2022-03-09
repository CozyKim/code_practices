# https://programmers.co.kr/learn/courses/30/lessons/60060


def solution(words, queries):
    answer = []
    word_lengths = {}
    # 트라이 초기화

    for word in words:
        # 정방향 트라이
        word_lengths[len(word)] = word_lengths.get(
            len(word),
            {
                "right": {"child": {}, "cnt": 0},
                "inv": {"child": {}, "cnt": 0},
            },
        )
        node = word_lengths[len(word)]["right"]
        for s in word:
            if s not in node["child"]:
                node["child"][s] = {"child": {}, "cnt": 0}
            node["cnt"] += 1
            node = node["child"][s]
        node["cnt"] += 1

        # 역방향 트라이
        node = word_lengths[len(word)]["inv"]
        for s in word[::-1]:
            if s not in node["child"]:
                node["child"][s] = {"child": {}, "cnt": 0}
            node["cnt"] += 1
            node = node["child"][s]
        node["cnt"] += 1

    def count_querie(querie):
        # 쿼리 물을표가 뒤에 있을때
        leng = word_lengths.get(len(querie), None)
        if leng == None:
            return 0
        if querie[0] != "?":
            node = word_lengths[len(querie)]["right"]
            for idx, s in enumerate(querie):
                if s == "?":
                    return node["cnt"]

                node = node["child"].get(s)
                if node == None:
                    return 0

        else:

            node = word_lengths[len(querie)]["inv"]

            for s in querie[::-1]:
                if s == "?":
                    return node["cnt"]

                node = node["child"].get(s)
                if node == None:
                    return 0

    for q in queries:
        answer.append(count_querie(q))
    print(word_lengths)
    print(answer)
    return answer


solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"],
)
