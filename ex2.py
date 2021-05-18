import time
import sys
from math import *
start = time.time()
def DrawStar(n):
    if n>3:
        N = n//3
        b = []
        a = DrawStar(N)
        for i in range(n):
            if i < N:
                b.append(3 * a[i])
            elif N <= i < N * 2:
                b.append(a[i-N] + N * ' ' + a[i-N])
            else:
                 b.append(3 * a[i - N*2])
        return b
    else:
        a = ['***', '* *', '***'] 
        return a
A = DrawStar(int(input()))
for i in range(len(A)):
    A.insert(2*i+1,'\n')
for i in A:
    # print(i, end= "")
    sys.stdout.write(i)
print("time : ",time.time() - start)
# 3초
