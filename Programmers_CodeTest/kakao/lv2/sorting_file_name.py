# https://programmers.co.kr/learn/courses/30/lessons/17686
import re


def solution(files):
    answer = []
    splited_files = []
    for name in files:
        splited_files.append(*re.findall("([\D]+)(\d+)(.*)", name))
    print(splited_files)
    for name in sorted(splited_files, key=lambda x: (x[0].lower(), int(x[1]))):
        answer.append("".join(name))
    return answer


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
)
