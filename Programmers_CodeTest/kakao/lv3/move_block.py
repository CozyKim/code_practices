from collections import deque


def solution(board):
    N = len(board)
    answer = 0
    dp = [
        [[float("inf"), float("inf")] for _ in range(len(board))]
        for _ in range(len(board))
    ]  # 가로, 세로
    dron_info = [[0, 1], 0]  # 드론 위치, 세로인지 여부

    q = deque([(0, 1, 0, 0)])
    while q:
        r, c, time, vertical = q.popleft()
        if (r, c) == (N - 1, N - 1):
            print(time)
            return time
        if dp[r][c][vertical] < time:
            continue
        dp[r][c][vertical] = time

        # 단순 이동
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if vertical == 0:
                    if not (0 <= nc - 1 < N) or board[nr][nc - 1] == 1:
                        continue
                else:
                    if not (0 <= nr - 1 < N) or board[nr - 1][nc] == 1:
                        continue
                if dp[nr][nc][vertical] > time + 1 and board[nr][nc] == 0:
                    dp[nr][nc][vertical] = time + 1
                    q.append((nr, nc, time + 1, vertical))

        # 회전
        # 앞에 있는 (r,c)를 기준으로 회전
        # 뒤에 있는 (r-1,c) or (r,c-1)를 기준으로 회전
        if vertical == 0:
            x, y = r, c - 1
            for dr in [1, -1]:
                nr, nc = r + dr, c
                nx, ny = x + dr, y
                if 0 <= nr < N and 0 <= nc < N:
                    if (
                        board[nr][c - 1] == 0
                        and dp[max(nr, r)][c][1] > time + 1
                        and board[nr][nc] == 0
                    ):
                        dp[max(nr, r)][c][1] = time + 1
                        q.append((max(nr, r), c, time + 1, 1))
                if 0 <= nx < N and 0 <= ny < N:
                    if (
                        board[nx][y + 1] == 0
                        and dp[max(nx, x)][y][1] > time + 1
                        and board[nx][ny] == 0
                    ):
                        dp[max(nx, x)][y][1] = time + 1
                        q.append((max(nx, x), y, time + 1, 1))
        else:
            x, y = r - 1, c
            for dc in [1, -1]:
                nr, nc = r, c + dc
                nx, ny = x, y + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if (
                        board[r - 1][nc] == 0
                        and dp[r][max(nc, c)][0] > time + 1
                        and board[nr][nc] == 0
                    ):
                        dp[r][max(nc, c)][0] = time + 1
                        q.append((r, max(nc, c), time + 1, 0))
                if 0 <= nx < N and 0 <= ny < N:
                    if (
                        board[x + 1][ny] == 0
                        and dp[x][max(ny, y)][0] > time + 1
                        and board[nx][ny] == 0
                    ):
                        dp[x][max(ny, y)][0] = time + 1
                        q.append((x, max(ny, y), time + 1, 0))

    return answer


solution(
    [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
)
