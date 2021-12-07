"""
- N 마리의 원숭이가 있다. 이들은 1~N 까지의 번호가 붙어있음
- 7일간 경기를 A와 B팀 나눠 하루에 한 번 진행
- 모든 원숭이 경기 참여해야함, 팀원 수는 달라도 됨
- 각 팀에서는 최소 한마리 원숭이 필요
- 모든 두 원숭이 대해서 적어도 한번은 적으로 만나도록

i번째 (날짜) 문자열의 j번째 문자는 i번째 날에 j번 원숭이가 속한 팀

메인 아이디어 : 
    1. 계속 반으로 나눠주면서 뒷부분은 반전 시키기
    2. 개수 N개를 최대한 반전 시키는 방법은 N <= 2^x 를 만족하는 x번 이다.
"""


def main():
    N = int(input())
    match_schdule = [[] for _ in range(7)]

    change = {"A": "B", "B": "A"}

    def div_and_change(before_match: list, len_a: int, step: int, last: int):
        if step > last:
            return

        # 반으로 나눴을 때 앞부분은 그대로 뒷부분은 반전 시키는 부분
        if len_a >= 2:
            a, b = (
                before_match[: len(before_match) // 2],
                before_match[len(before_match) // 2 :],
            )
        else:
            a, b = before_match, []
        b = list(map(lambda x: change[x], b))
        match_schdule[step].extend(a)
        match_schdule[step].extend(b)
        div_and_change(a, len(a), step + 1, last)
        div_and_change(b, len(b), step + 1, last)

    # 7일간 경기를 하니 2^1 ~ 2^7 까지 기준을 제시
    basis = [2, 2 ** 2, 2 ** 3, 2 ** 4, 2 ** 5, 2 ** 6, 2 ** 7]

    last = None
    for idx, i in enumerate(basis):
        if N // i == 0 or N == i:
            last = idx
            break
    div_and_change(["A"] * N, N, 0, last)
    for match in match_schdule:
        # 비어 있을 경우 각 팀에 최소 한마리가 있는 경우를 아무거나 넣으면 되니 A 하나랑 나머지 B
        if not match:
            match.extend(["A"] + ["B" for _ in range(N - 1)])
        print("".join(match))


if __name__ == "__main__":
    main()
