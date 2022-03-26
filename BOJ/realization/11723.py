# https://www.acmicpc.net/problem/11723

"""
문제 설명
    비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

    add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    all: S를 {1, 2, ..., 20} 으로 바꾼다.
    empty: S를 공집합으로 바꾼다. 

입력 
    첫쨰 줄 : 연한을 수행해야하는 연산 수 M
    둘째 줄 : M개의 줄에 수행해야하는 연산이 한줄에 하나씩

출력
    check 연산이 주어질 때 마마다 연산이 한 줄 씩 주어진다.
"""
import sys

input = sys.stdin.readline

sets = 0


def op_add(sets, x):
    sets = sets | 2 ** (x - 1)
    return sets


def op_remove(sets, x):
    sets = sets & ~(2 ** (x - 1))
    return sets


def op_check(sets, x):
    check = str(bin(sets))[2:]
    if len(check) > x - 1 and int(check[x - 1]):
        print(1)
    else:
        print(0)


def op_toggle(sets, x):
    sets = sets ^ (2 ** (x - 1))
    return sets


def op_all():
    sets = 1048575
    return sets


def op_empty():
    return 0


M = int(input())
for _ in range(M):
    ops = input().split()
    try:
        op, n = ops[0], int(ops[-1])
    except:
        op = ops[0]
    if op == "add":
        sets = op_add(sets, n)
    elif op == "remove":
        sets = op_remove(sets, n)
    elif op == "check":
        op_check(sets, n)
    elif op == "toggle":
        sets = op_toggle(sets, n)
    elif op == "all":
        sets = op_all()
    elif op == "empty":
        sets = op_empty()
