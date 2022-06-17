# https://www.acmicpc.net/problem/1918

string = input()
answer = ""
stack = []

for s in string:
    if s == "(":
        stack.append("|")
    elif s == ")":
        while stack and stack[-1] != "|":
            answer += stack.pop()
        stack.pop()

    elif s in "*/":
        while stack and stack[-1] in "*/":
            answer += stack.pop()
        stack.append(s)
    elif s in "+-":
        while stack and stack[-1] != "|":
            answer += stack.pop()
        stack.append(s)

    else:
        answer += s

while stack:
    answer += stack.pop()

print(answer)
