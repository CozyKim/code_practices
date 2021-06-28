# https://programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    answer = []

    arr = [[i*columns + j+1 for j in range(columns)] for i in range(rows)]
    # print(arr)

    def rotate(x1, y1, x2, y2):
        _tmp = []
        m = y2 - y1
        n = x2 - x1
        tmp1 = arr[x1][y1]
        tmp2 = arr[x2][y2]
        _tmp += [tmp1, tmp2]
        for i in range(1, m+1):
            tmp = arr[x1][y1+i]
            arr[x1][y1+i] = tmp1
            tmp1 = tmp

            tmp = arr[x2][y2-i]
            arr[x2][y2-i] = tmp2
            tmp2 = tmp
            _tmp += [tmp1, tmp2]

        for i in range(1, n+1):
            if i == 1:
                tmp3 = arr[x1+i][y2]
                arr[x1+i][y2] = tmp1

                tmp4 = arr[x2 - i][y1]
                arr[x2 - i][y1] = tmp2
                _tmp += [tmp3, tmp4]
            else:
                tmp = arr[x1+i][y2]
                arr[x1+i][y2] = tmp3
                tmp3 = tmp

                tmp = arr[x2-i][y1]
                arr[x2-i][y1] = tmp4
                tmp4 = tmp
                _tmp += [tmp3, tmp4]

        return min(_tmp)

    for x1, y1, x2, y2 in queries:
        answer.append(rotate(x1-1, y1-1, x2-1, y2-1))

    print(arr)
    print(answer)
    return answer


solution(100, 97, [[1, 1, 100, 97]])
