# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
def solution(num):
    num = list(map(str, num))
    num.sort(key=lambda x: x*3,
             reverse=True)
    return str(int(''.join(num)))


solution([1, 0, 1, 11, 131, 1000, 2, 242, 212, 21, 24,
         42, 220, 221, 222, 223, 234, 234, 224, 0, 0])
