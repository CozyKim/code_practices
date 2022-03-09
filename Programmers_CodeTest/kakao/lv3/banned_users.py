# https://programmers.co.kr/learn/courses/30/lessons/64064


def solution(user_id, banned_id):
    answer = {}

    def check(user_idx, check_id):
        candid = []
        for idx in user_idx:
            if len(user_id[idx]) == len(check_id):
                for u, b in zip(user_id[idx], check_id):
                    if b == "*":
                        continue
                    if u != b:
                        break
                else:
                    candid.append(idx)
        return candid

    def dfs(u_idxs: list, b_idx: int):
        nonlocal answer
        if b_idx == len(banned_id):
            cand = tuple(sorted(set(user_index) - set(u_idxs)))
            if cand in answer:
                return
            answer[cand] = 1
            return

        for c in check(u_idxs, banned_id[b_idx]):
            dfs(list(set(u_idxs) - set([c])), b_idx + 1)

    user_index = [i for i in range(len(user_id))]
    dfs(user_index, 0)

    return answer


print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"],
    )
)
