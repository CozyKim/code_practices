# https://programmers.co.kr/learn/courses/30/lessons/60062

from bisect import bisect_left, bisect_right


def solution(n, weak, dist):
    answer = float("inf")
    dist.sort(reverse=True)
    if dist[0] >= n - 1:
        return 1
    dp = [[float("inf")] * len(weak) for _ in range(len(dist))]

    def dfs(left_weak, dist_idx):
        nonlocal answer
        if dist_idx >= answer:
            return

        if not left_weak:
            answer = dist_idx
        if dist_idx == len(dist):
            return
        for weak_v in left_weak:
            if dp[dist_idx][bisect_left(weak, weak_v)] < len(left_weak) - 1:
                continue
            dp[dist_idx][bisect_left(weak, weak_v)] = len(left_weak) - 1
            if weak_v + dist[dist_idx] < n:
                dist_end = weak_v + dist[dist_idx]
                dist_end_idx = (
                    bisect_left(weak, dist_end) + 1
                    if dist_end in left_weak
                    else bisect_left(weak, dist_end)
                )
                dfs(
                    left_weak - set(weak[bisect_left(weak, weak_v) : dist_end_idx]),
                    dist_idx + 1,
                )
            else:
                dist_end = weak_v + dist[dist_idx] - n
                dist_end_idx = (
                    bisect_left(weak, dist_end) + 1
                    if dist_end in left_weak
                    else bisect_left(weak, dist_end)
                )

                dfs(
                    left_weak
                    - (
                        set(weak[:dist_end_idx])
                        | set(weak[bisect_left(weak, weak_v) :])
                    ),
                    dist_idx + 1,
                )

    dfs(set(weak), 0)
    return answer if answer != float("inf") else -1


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
