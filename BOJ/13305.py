import sys
N = int(sys.stdin.readline())
Road = list(map(int, sys.stdin.readline().split()))
Town = list(map(int, sys.stdin.readline().split()))
lowest_Town = Town[0]
cost = 0
check_point = []
for i in range(len(Town)):
    if Town[i] <= lowest_Town:
        check_point.append(i)
        lowest_Town = Town[i]
for i in range(len(check_point)):
    if i == len(check_point) - 1:
        tmp_Road = Road[check_point[i]:]
    else:
        tmp_Road = Road[check_point[i]:check_point[i+1]]
    cost += sum(tmp_Road) * Town[check_point[i]]
print(cost)
