def init():
    L, C, R, U, D = 4, 1, 3, 5, 2
    return L, C, R, U, D


def move_right(L, C, R, U, D):
    l, c, r, u, d = 7 - C, L, C, U, D
    return l, c, r, u, d


def move_left(L, C, R, U, D):
    l, c, r, u, d = C, R, 7 - C, U, D
    return l, c, r, u, d


def move_down(L, C, R, U, D):
    l, c, r, u, d = L, U, R, 7 - C, C
    return l, c, r, u, d


row, column = map(int, input().split())
column1 = 0
column2 = column

if column > 4:
    column1 = column // 4
    column2 = column % 4
    if column % 4 == 0:
        column2 = 4
        column1 = column // 4 - 1

L, C, R, U, D = init()
result = C
for i in range(row):
    for j in range(column2 - 1):
        if i % 2 == 0:
            L, C, R, U, D = move_right(L, C, R, U, D)
            result += C
        else:
            L, C, R, U, D = move_left(L, C, R, U, D)
            result += C
    if i != row - 1:
        L, C, R, U, D = move_down(L, C, R, U, D)
        result += C
result += column1 * 14 * row
print(result)
