# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo


from copy import deepcopy


def break_block(x, y):
    global visited
    if visited[x][y]:
        return
    visited[x][y] = 1
    for i in range(1, board[x][y]):
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + i * dx, y + dy * i
            if 0 <= nx < H and 0 <= ny < W:
                break_block(nx, ny)


def update():
    for c in range(W):
        stack = []
        for r in range(H):
            if not visited[r][c] and board[r][c]:
                stack.append(board[r][c])
            if visited[r][c]:
                visited[r][c] = 0
            board[r][c] = 0
        r = H - 1
        while stack:
            block = stack.pop()
            board[r][c] = block
            r -= 1


def count_block():
    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j]:
                cnt += 1
    return cnt


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, W, H = map(int, input().split())
    BOARD = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    answer = float("inf")
    orders = []
    for i in range(W ** N):
        tmp = []
        for j in range(N - 1, -1, -1):
            o, i = divmod(i, W ** j)
            tmp.append(o)
        orders.append(tmp)
    for order in orders:

        board = deepcopy(BOARD)
        for c in order:
            r = 0
            while r < H and not board[r][c]:
                r += 1
            if r == H:
                break
            break_block(r, c)
            update()
        a = count_block()
        answer = min(answer, a)
        if answer == 0:
            break
    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
