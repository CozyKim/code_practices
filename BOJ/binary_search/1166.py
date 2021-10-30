"""민식이는 아이들에게 선물할 같은 크기의 작은 박스를 N개 가지고 있다. 모든 작은 박스는 정육면체이고, 
크기는 A × A × A 이다. 민식이는 이 작은 박스를 크기가 L × W × H 인 직육면체 박스에 모두 넣으려고 한다. 
모든 작은 박스는 큰 박스 안에 있어야 하고, 작은 박스의 변은 큰 박스의 변과 평행해야 한다.

N, L, W, H가 주어질 때, 가능한 A의 최댓값을 찾는 프로그램을 작성하시오."""

"""pesudo code
1. 부피는 전체 부피가 같으면 되니 N * A*A*A = L*W*H 인 A를 구하면 되는 것 아닌가? 
    -> X : 문제 이해를 제대로 안함 - 꽉 안차도 되고 A를 `최대화` 하는 값을 찾아야 한다!

2. N <= (L//A) * (W//A) * (H//A) , A <= min(L,W,H) 를 만족하는 최대 A
    A는 최대 크기인 min(L,W,H)부터 시작    
"""

# 1
# N, L, W, H = map(int, input().split())
# A = (L * W * H / N) ** (1 / 3)
# B = pow(L * W * H / N, 1 / 3)

# print(A)
# print(B)

# 2
N, L, W, H = map(int, input().split())

threshold = 1e-10  #  "절대/상대 오차는 10-9까지 허용" 이라 했는데 왜 통과가 안될까..
A = float(min(L, W, H))
last_A = 0
MIN = 0
MAX = min(L, W, H)
while abs(last_A - A) >= threshold:

    if N > (L // A) * (W // A) * (H // A):  # A가 더 감소 해야한다.
        last_A = A
        MAX = A
        A = (MIN + A) / 2
    else:  # A가 더 증가 해야한다.
        last_A = A
        MIN = A
        A = (MAX + A) / 2

print(A)
