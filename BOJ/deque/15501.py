# https://www.acmicpc.net/problem/15501
"""
1~n 까지의 수가 한 번만 사용된 수열 주어짐
그 수열을 뒤집기, 밀기 (오른쪽, 왼쪽) 을 통해 세번째 주어지는 수열을 구성할 수 있는지 확인
"""

"""
뒤집기를 두 번하면 처음꺼랑 같아지니 한번만 사용한다.
한쪽으로만 쭉 밀어도 순환(모든 경우를 다 볼 수 있음)
전체를 다 비교하기에는 시간이 오래 걸림, 모든 수가 한 번만 사용한다고 했으니 첫 자리수만 비교
"""

from collections import deque


def main():
    n = int(input())
    basis = input().split()
    goal = input().split()
    basis = deque(basis)
    rev_basis = deque(reversed(basis))
    for _ in range(len(basis)):
        if basis[0] == goal[0]:
            if list(basis) == goal:
                return "good puzzle"
        elif rev_basis[0] == goal[0]:
            if list(rev_basis) == goal:
                return "good puzzle"
        tmp = basis.popleft()
        basis.append(tmp)
        tmp = rev_basis.popleft()
        rev_basis.append(tmp)
    else:
        return "bad puzzle"


print(main())
