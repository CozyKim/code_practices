import re
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    code = input().strip()
    answer = re.match("^[A-F]?A+F+C+([A-F]?)$", code)
    if answer != None:
        print("Infected!")
    else:
        print("Good")
