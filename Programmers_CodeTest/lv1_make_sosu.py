def solution(nums: list):
    answer = 0
    nums.sort()
    nums_odd = [i for i in nums if i % 2 != 0]
    nums_even = [i for i in nums if i % 2 == 0]
    # 홀 홀 홀
    for i in range(len(nums_odd)-2):
        for j in range(i+1, len(nums_odd)-1):
            for k in range(j+1, len(nums_odd)):
                if check_prime_num(nums_odd[i]+nums_odd[j]+nums_odd[k]):
                    answer += 1
    # 짝 홀 홀
    for i in range(len(nums_odd)):
        for j in range(len(nums_even)-1):
            for k in range(j+1, len(nums_even)):
                if check_prime_num(nums_odd[i]+nums_even[j]+nums_even[k]):
                    answer += 1

    return answer


def check_prime_num(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
