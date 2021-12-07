"""
    접는 방법 - 동호의 규칙
    1. 오른쪽 반을 반시계 방향으로 접어서 왼쪽 반의 위로 접음 (IN)
    2. 오른쪽 반을 시계 방향으로 접어서 왼쪽 반의 아래로 접음 (OUT)
    종이를 안 접을 수도 있다.

    종이가 접혀있는 정보가 왼쪽부터 오른쪽까지 차례대로 주어졌을 때, 이 종이를 동호의 규칙대로 접을 수 있는지 없는지를 구하는 프로그램을 작성하시오.

    input : 1(OUT), 0(IN)
    output : 차례대로 동호의 규칙을 적용해서 접을 수 있는가?

풀이 메인 아이디어 :
    한번 접을 때 마다 이존에 있던 것들 사이에 양쪽으로 서로 방향이 반대인 것들이 생긴다
    예시) 1 -> 011 -> 1001100
"""
import sys

input = sys.stdin.readline


def dongho_rule(nums: str):

    if len(nums) < 3:
        # 한번 만 접었을 때
        return True

    next_nums = ""
    for i in range(2, len(nums), 2):
        # 0부터 2의 배수 만큼 서로 비교하여 방향이 반대가 아니면 동호의 규칙이 적용이 안된다
        if nums[i - 2] == nums[i]:
            return False
        next_nums += nums[i - 1]  # 가장 마지막에 접었던 것을 안 접었다 생각하기
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
