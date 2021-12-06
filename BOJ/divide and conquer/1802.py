"""
    접는 방법 - 동호의 규칙
    1. 오른쪽 반을 반시계 방향으로 접어서 왼쪽 반의 위로 접음 (IN)
    2. 오른쪽 반을 시계 방향으로 접어서 왼쪽 반의 아래로 접음 (OUT)
    종이를 안 접을 수도 있다.

    종이가 접혀있는 정보가 왼쪽부터 오른쪽까지 차례대로 주어졌을 때, 이 종이를 동호의 규칙대로 접을 수 있는지 없는지를 구하는 프로그램을 작성하시오.

    input : 1(OUT), 0(IN)
    output : 차례대로 동호의 규칙을 적용해서 접을 수 있는가?

"""
import sys

input = sys.stdin.readline


def dongho_rule(nums: str):

    if len(nums) < 3:
        return True

    next_nums = ""
    for i in range(2, len(nums), 2):
        if nums[i - 2] == nums[i]:
            return False
        next_nums += nums[i - 1]
    next_nums += nums[len(nums) - 1]

    if dongho_rule(next_nums):
        return True
    else:
        return False


T = int(input())

for _ in range(T):
    paper = input().strip()
    if dongho_rule(paper):
        print("YES")
    else:
        print("NO")
