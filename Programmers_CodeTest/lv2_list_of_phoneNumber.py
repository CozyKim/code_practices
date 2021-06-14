# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
def solution(phone_book: list):
    answer = True
    phone_book.sort()
    for idx, num in enumerate(phone_book):
        if idx == 0:
            pass
        else:
            if num[:len(phone_book[idx-1])] == phone_book[idx-1]:
                return False

    return answer


solution(["123", "456", "789"])
