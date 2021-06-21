# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

def solution(begin, target, words):
    answer = 0

    def check_spel(origin, target):
        cnt = 0
        for a, b in zip(origin, target):
            if a is b:
                cnt += 1
        if cnt == len(origin)-1:
            return True
        else:
            return False

    counts = []

    def DFS(begin, target, visited=[], cnt=0):
        if begin == target:
            counts.append(cnt)

            return
        if begin not in visited:
            for tar in words:
                if begin is tar:
                    continue
                if check_spel(begin, tar) and tar not in visited:
                    DFS(tar, target, visited + [begin], cnt + 1)
        return

    DFS(begin, target)
    if len(counts) == 0:
        # print(0)
        return 0
    else:
        # print(min(counts))
        return min(counts)


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
