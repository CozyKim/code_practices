import sys


class Stack:
    def __init__(self) -> None:
        self.__stk = []

    def Push(self, X):
        return self.__stk.append(X)

    def Pop(self):
        if not self.__stk:
            return -1
        else:
            return self.__stk.pop()

    def Size(self):
        return len(self.__stk)

    def Empty(self):
        if not self.__stk:
            return 1
        else:
            return 0

    def Top(self):
        if self.Empty():
            return -1
        else:
            return self.__stk[self.Size()-1]


N = int(sys.stdin.readline())
S = Stack()
for _ in range(N):
    Order = sys.stdin.readline().rstrip().split()
    if Order[0] == 'push':
        S.Push(int(Order[1]))
    elif Order[0] == 'pop':
        print(S.Pop())
    elif Order[0] == 'size':
        print(S.Size())
    elif Order[0] == 'empty':
        print(S.Empty())
    elif Order[0] == 'top':
        print(S.Top())
