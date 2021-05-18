########################################################
# 단기간 성장 

# 12865번
# N 개의 물건, 
# 각 물건 : 무게 W, 가치 V
# 최대 무게 K
# 최대 V는?

# import sys

# def backpack(wv, k):
#     mem = [None]*(len(wv)+1)
#     for i in range(len(wv)+1):
#         mem[i]=[None]*(k+1)
#     for i in range(len(wv)+1):
#         for j in range(k+1):
#             if i == 0 or j == 0:
#                 mem[i][j] = 0
#             elif wv[i-1][0] > j:
#                 mem[i][j] = mem[i-1][j]
#             else:
#                 mem[i][j] = max(mem[i-1][j], mem[i-1][j-wv[i-1][0]]+wv[i-1][1])
#     return mem[len(wv)][k]
# N, K = map(int, sys.stdin.readline().split())
# WV=[None] * N
# for i in range(N):
#     WV[i]= list(map(int, sys.stdin.readline().split()))
# print(backpack(WV, K))

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
r={0:0}
for _ in range(n):
    w,c=map(int,input().split())
    if w<=m:
        for j,v in list(r.items()):
            if w+j<=m:
                if w+j in r.keys():r.update({w+j:max(c+v,r[w+j])})
                else :r.update({w+j:c+v})
print(max(r.values()))