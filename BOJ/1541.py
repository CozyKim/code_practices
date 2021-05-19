import sys

flag = 0
tmp = 0
minus_num = []
plus_num = []
S = sys.stdin.readline().rstrip()
for i in range(len(S)):
    if i == len(S)-1:
        if flag:
            minus_num.append(int(S[tmp:]))
        else:
            plus_num.append(int(S[tmp:]))
    else:
        if S[i] == '-':
            if flag:
                minus_num.append(int(S[tmp:i]))
                tmp = i+1
            else:
                plus_num.append(int(S[tmp:i]))
                tmp = i+1
                flag = 1

        elif S[i] == '+':
            if flag:
                minus_num.append(int(S[tmp:i]))
                tmp = i+1
            else:
                plus_num.append(int(S[tmp:i]))
                tmp = i+1
print(sum(plus_num)-sum(minus_num))
