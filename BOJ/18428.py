import sys
from itertools import combinations
input = sys.stdin.readline


def check(teachers, students, ob_list):
    obstacle = [[0 for _ in range(N)] for _ in range(N)]
    for i, j in ob_list:
        obstacle[i][j] = 1
    num = len(teachers)
    for t_pos in teachers:
        for s_pos in students:
            flag = 1
            if t_pos[0] == s_pos[0]:
                if t_pos[1] > s_pos[1]:
                    for i in range(s_pos[1]+1, t_pos[1]):
                        if obstacle[t_pos[0]][i] == 1:
                            flag = 0
                            break
                    if flag:
                        return False

                elif t_pos[1] < s_pos[1]:
                    for i in range(t_pos[1]+1, s_pos[1]):
                        if obstacle[t_pos[0]][i] == 1:
                            flag = 0
                            break
                    if flag:
                        return False
            elif t_pos[1] == s_pos[1]:
                if t_pos[0] > s_pos[0]:
                    for i in range(s_pos[0]+1, t_pos[0]):
                        if obstacle[i][t_pos[1]] == 1:
                            flag = 0
                            break
                    if flag:
                        return False
                elif t_pos[0] < s_pos[0]:
                    for i in range(t_pos[0]+1, s_pos[0]):
                        if obstacle[i][t_pos[1]] == 1:
                            flag = 0
                            break
                    if flag:
                        return False
    return True


tile = []
N = int(input())
students = []
teachers = []
tiles = []
for i in range(N):
    tile = input().rstrip().split()
    for j, t in enumerate(tile):
        if t == 'X':
            tiles.append((i, j))
        elif t == 'S':
            students.append((i, j))
        elif t == 'T':
            teachers.append((i, j))
tmp = set()
for t in teachers:
    for i in range(N):
        tmp |= set([(i, t[1])])
        tmp |= set([(t[0], i)])
# tmptmp = [[0 for _ in range(N)] for _ in range(N)]
tmp -= set(students)
tmp -= set(teachers)
# for i, j in tmp:
# tmptmp[i][j] = 1
ob_list = list(combinations(tmp, 3))
flag = 1
for ob in ob_list:
    if check(teachers, students, ob):
        print('YES')
        flag = 0
        break
if flag:
    print('NO')
