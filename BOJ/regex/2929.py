import re
import math

code = input()
find = re.findall("[A-Z][a-z]*", code)
# finditer 사용해보기
cnt = 0
for i, s in enumerate(find):
    if i == len(find) - 1:
        continue
    cnt += 4 * math.ceil(len(s) / 4) - len(s)
print(cnt)
