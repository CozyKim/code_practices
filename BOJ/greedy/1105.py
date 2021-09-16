L, R = input().split()
if len(R) - len(L) > 0:
    result = 0
else:
    tmp = ''
    for l, r in zip(L, R):
        if l == r:
            tmp += l
        else:
            break
    result = tmp.count('8')
print(result)
