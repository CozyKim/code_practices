import sys
Alhpa = []
Numb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
N = int(sys.stdin.readline())
num = 9
for _ in range(N):
    Alhpa.append(sys.stdin.readline().rstrip())
Alhpa.sort(reverse=True, key=lambda x: len(x))
for t in range(len(Alhpa)):
    if len(Alhpa[0]) != len(Alhpa[t]):
        Alhpa[t] = ' ' * (len(Alhpa[0]) - len(Alhpa[t])) + Alhpa[t]
for i in range(len(Alhpa[0])):
    for k in range(N):
        if Alhpa[k][i] == ' ' or Alhpa[k][i] in Numb:
            continue
        else:
            Alhpa = str(Alhpa).replace(Alhpa[k][i], str(num))
            Alhpa = eval(Alhpa)
            num -= 1
Alhpa = list(map(int, Alhpa))
print(sum(Alhpa))
