import sys

input = sys.stdin.readline
N = int(input())
pattern = input().rstrip()
star_idx = pattern.index('*')
al_1 = pattern[:star_idx]
al_2 = pattern[star_idx+1:]

for _ in range(N):
    text = input().rstrip()
    if len(text) < len(al_1) + len(al_2):
        print('NE')
    elif text[:len(al_1)] == al_1 and text[-len(al_2):] == al_2:
        print('DA')
    else:
        print('NE')
