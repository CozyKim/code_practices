def solution(s):
    answer = float("inf")
    for i in range(1, len(s)):
        prev = s[0:i]
        cnt = 1
        compressed_s = ""
        for j in range(i, len(s), i):
            word = s[j : j + i]
            if not word:
                break
            if word == prev:
                cnt += 1
            else:
                if cnt == 1:
                    compressed_s += prev
                else:
                    compressed_s += str(cnt) + prev
                cnt = 1
            prev = word
        compressed_s += str(cnt) + prev if cnt > 1 else prev
        answer = min(answer, len(compressed_s))

    return answer if len(s) > 1 else 1
