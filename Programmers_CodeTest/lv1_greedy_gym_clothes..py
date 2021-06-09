
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lost_ = lost[:]
    nums = []
    cnt = 0
    for l in lost_:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
            continue
        nums = add_(nums, l)
    for r in reserve:
        if r in nums:
            idx = nums.index(r)//3 + cnt
            nums = popping(nums, lost[idx])
            cnt += 1
    answer = n - len(lost) + cnt
    return print(answer)


def add_(lst: list, n: int):
    lst.append(n-1)
    lst.append(n)
    lst.append(n+1)
    return lst


def popping(lst: list, n: int):
    lst.remove(n-1)
    lst.remove(n)
    lst.remove(n+1)
    return lst


solution(8, [4, 5], [5, 6])
