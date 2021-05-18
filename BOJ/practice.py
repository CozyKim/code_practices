# h, m= map(int, input().split())

# case = []
# test_num = int(input())
# for num in range(1,test_num+1):
#     a, b = map(int,input().split())
#     case.append(a+b)

# for num in range(0,test_num):
#     print(case[num])

# n = int(input())
# A=0
# for i in range(1,n+1):
#     A+=i
# print(A)

# from sys import stdin as std
# t = int(std.readline().rstrip())

# for num in range(0,t):
#     a, b = map(int,std.readline().rstrip().split())
#     print(a+b)

# n = int(input())
# for i in range(1, n+1):
#     print(" "*(n-i),"*"*i)
# import sys
# N =int(sys.stdin.readline())
# A=[]
# B=[]
# for i in range(1,N+1):
#     print("{0}".format(str(i*"*").rjust(N)))

# n, x = map(int,input().split())
# A= list(range(n))
# A = list(map(int,input().split()))
# for i in A:
#     if i<x:
#         print(i, end=" ")

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break


# n = int(input())
# cycle = 0
# flag = 0
# x1 = n
# while flag == 0 :
#     try:
#         if 0 <= n <= 99:
#             x2 = int(x1/10) + x1%10
#             x2 = x1%10*10+x2%10
#             x1 = x2
#             cycle += 1
#             if x1 == n:
#                 flag = 1
#     except:
#         break
# print(cycle)

# from sys import stdin as std
# n = int(std.readline().rstrip())
# A = []
# A = list(map(int,std.readline().rstrip().split()))
# print(min(A), max(A))

# a=[]
# for i in range(9):
#     a.append(int(input()))
# print(max(a))
# print(a.index(max(a))+1)



# 2577
# a = int(input())
# b = int(input())
# c = int(input())
# A = str(a*b*c)
# for i in range(10):
#     print(A.count(str(i)))



# 1546번
# n = int(input())
# socres = list(map(int, input().split()))
# max_score = max(socres)
# for i in range(n):
#     socres[i] = socres[i]/max_score * 100
# print(sum(socres)/n)



# 8958번
# import sys
# case = int(sys.stdin.readline())
# test=[]
# score = 0
# scores = 0
# for i in range(case):
#     test.append(sys.stdin.readline())
# for i in range(case):
#     scores = 0
#     score = 0 
#     for x in test[i]:
#         if x == "O":
#             score += 1
#             scores += score
#         elif x == "X":
#             score = 0
#     print(scores)
    

# 4344번
# c = int(input())
# N =[]
# count = 0
# for i in range(c):
#     N = list(map(int, input().split()))
#     mean_ = sum(N[1:])/N[0]
#     for x in N[1:]:
#         if x > mean_:
#             count +=1
#     print("{:.3f}%".format(count/N[0]*100))
#     count = 0 
#     N = []

# import sys
# c = int(input())
# N =[]
# count = 0
# for i in range(c):
#     N = list(map(int,sys.stdin.readline().split()))
#     mean_ = sum(N[1:])/N[0]
#     for x in N[1:]:
#         if x > mean_:
#             count +=1
#     print(str(round(count/N[0]*100,3))+"%")
#     count = 0 
#     N = []


# 15596번
# def solve(a: list):
#     sum = 0
#     for i in a:
#         sum +=i
#     return int(sum)

# # 4673번
# def NotSelfNumber(N):
#     ans = N
#     leng = len(str(N))
#     for i in range(leng):
#         ans += int(str(N)[i])
#     return ans
# n=1
# chack = []
# while n<10000:
#     chack.append(NotSelfNumber(n))
#     if chack.count(n) == 0:
#         print(n)
#     n += 1



# # 1065번
# n = int(input())
# count = 0
# count_sub = 0
# for i in range(1,n+1):
#     i_ = str(i)
#     for k in range(len(i_)):
#         if k == 0:
#             continue
#         sub = int(i_[k]) - int(i_[k-1])
#         if k == 1:
#             temp = sub    
#         if temp == sub:
#             count_sub += 1
#         temp = sub
#     if count_sub == len(i_) - 1:
#         count += 1
#     count_sub = 0
# print(count)



# # 11654번
# x = input()
# print(ord(x))
        
# # 11720번
# N = int(input())
# n = int(input())
# n_ = str(n)
# sum = 0
# for i in n_:
#     sum += int(i)
# print(sum)


# 10809번
# import sys
# s = sys.stdin.readline()
# for i in range(ord('a'),ord('z')+1):
#     print(s.find(chr(i)), end=" ")



# # 2675번
# import sys
# t = int(input())
# for i in range(t):
#     r, s = sys.stdin.readline().split()
#     for k in range(len(s)):
#         print(s[k]*int(r), end="")
#     print()


# 1157번
# import sys
# s = sys.stdin.readline().rstrip()
# s = s.upper()
# count = 0
# A = []
# for i in range(ord('A'),ord('Z')+1):
#     A.append(s.count(chr(i)))
# if A.count(max(A)) == 1:
#     print(chr(ord('A') + A.index(max(A))))
# else :
#     print("?")

# # 1152반
# import sys
# s = sys.stdin.readline().rstrip().split()
# a = len(s)
# print(a)


# # 2908번
# def Reverse(a):
#     temp = ''
#     for i in range(len(a)):
#         temp += a[len(a)-1-i]
#     return int(temp)
# import sys
# a , b = sys.stdin.readline().rstrip().split()
# a = Reverse(a)
# b = Reverse(b)
# if a > b:
#     print(a)
# else :
#     print(b)


# # 5622번
# import sys
# S = sys.stdin.readline().rstrip()
# count = 0
# for s in S:
#     if s == 'A' or s =='B' or s =='C':
#         count += 3  # 2
#     elif s == 'D' or s =='E' or s =='F':
#         count += 4  # 3
#     elif s == 'G' or s == 'H' or s == 'I':
#         count += 5  # 4
#     elif s == 'J' or s == 'K' or s == 'L':
#         count += 6  # 5
#     elif s == 'M' or s == 'N' or s == 'O':
#         count += 7  # 6
#     elif s == 'P' or s == 'Q' or s == 'R' or s == 'S':
#         count += 8  # 7
#     elif s == 'T' or s == 'U' or s == 'V' :
#         count += 9
#     elif s == 'W' or s == 'X' or s == 'Y' or s == 'Z':
#         count += 10
#     else:
#         count += 11
# print(count)


# 2941번
# import sys
# s = sys.stdin.readline().rstrip()
# count = 0
# alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# for i in alphabet:
#     count += s.count(i)
#     s = s.replace(i," ")
# s = s.replace(" ","")
# count += len(s)
# print(count)


# # 1316번
# import sys
# def GroupWord(a):
#     flag = 1
#     cnt = 0
#     for i in range(ord('a'),ord('z')+1):
#         i = chr(i)
#         for k in range(len(a)):
#             if a[k] == i:
#                 cnt += 1
#                 try:
#                     if a[k+1] != i:
#                         break
#                 except:
#                     pass
#         if cnt != a.count(i):
#             flag = 0
#             break
#         cnt = 0
#     return flag
        

# n = int(input())
# count = 0
# for i in range(n):
#     word = sys.stdin.readline().rstrip()
#     count += GroupWord(word)
# print(count)


# # 1712번
# # A 고정비용 , B : 가변비용
# import sys
# from math import floor
# A, B, C = map(int, sys.stdin.readline().split())
# if C-B <= 0:
#     print(-1)
# else:
#     print(floor(A / (C - B))+1) 


# 2292번
# # 1, 7, 19, 37, 61
# # +6 +12 +18 +24
# def Bee_House(n):
#     room = 1
#     if n == 1:
#         return 1
#     for i in range(n):
#         room += 6*i
#         if n <= room:
#             return i+1
# N = int(input())
# print(Bee_House(N))


# 1193번
# 1, 3, 4, 10, 11, 21, 
# 대각션 별로 분모 분자 합이 같다
# 1, 5, 13, 

# def program(n):
#     cnt = 1
#     for i in range(1,n+1):
#         if cnt >= n:
#             i_ = i
#             break
#         cnt += i +1
#     N = cnt - n
#     if i_%2 !=0:
#         return print("{}/{}".format(1 + N, i_ - N))
#     else:
#         return print("{}/{}".format(i_ - N, 1 + N))
        
# s = int(input())
# program(s)



# # 2869번 
# import sys
# A, B, V = map(int,sys.stdin.readline().rstrip().split())
# # if (V - A) / (A - B)> 0:
# if int((V - A) / (A-B)) == float((V - A) / (A-B)):
#     days = int((V - A) / (A-B)) +1
# else:   
#     days = int((V - A) / (A-B)) +2
# # else:
# #     days = 1
# print(days)


# 10250번
# def CountRoom(h, w, n):
#     w = str(w)
#     if int(n/h) == n/h:
#         room_num = str(int(n/h))
#     else:
#         room_num = str(int(n/h) + 1)
#     room_floor = n%h
#     if room_floor == 0:
#         room_floor = h
#     zeros = len(w)-len(room_num)
#     if len(w) == 1:
#         zeros = 1
#     room_floor = str(room_floor)
#     room_num = str(room_num)
#     return room_floor+zeros*"0"+room_num


# T = int(input())
# for i in range(T):
#     H, W, N = map(int, input().split())
#     print(CountRoom(H, W, N))



# 2775번
# def Num(K,N):
#     underfloor = list(range(1,N+1))
#     currentfloor = list(range(1,N+1))
#     for k in range(K):
#         for n in range(N):
#             currentfloor[n] = sum(underfloor[:n+1])
#         underfloor = currentfloor[0:]
#     return currentfloor[N-1]
# T = int(input())
# for i in range(T):
#     k = int(input()) # 층
#     n = int(input()) # 호
#     print(Num(k,n))



# # 2839번

# # def Cnt_Kg(n):
# #     A = []
# #     for a in range(int(n/5)+1):
# #         for b in range(int(n/3)+1):
# #             if 5*a + 3*b == n:
# #                 A.append(a+b)
# #     if len(A) == 0:
# #         return  -1
# #     return min(A)
# def Cnt_Kg(kg):
#     box = 0
#     while True:
#         if kg%5 == 0:
#             box += kg//5
#             return box
#         box += 1
#         kg -= 3
#         if kg < 0:
#             return -1
# import sys
# N = int(sys.stdin.readline())
# print(Cnt_Kg(N))
# # 3, 5 kg 봉지



# # 10757번

# import sys
# A, B = map(int, sys.stdin.readline().rstrip().split())
# print(A+B)


# # 1011번

# # y 지점 도착 직전 속도는 1 
# # x 에서 처음 시작 속도 1만 움직일 수 있다
# # 이전에 k -> 다음에 k-1, k, k+1 가능
# import sys
# def Count(x, y):
#     num = 0
#     cnt = 0
#     for i in range(1,y+1):
#         for k in range(2):
#             num += i
#             cnt += 1
#             if y-x <= num:
#                 return print(cnt)

# T = int(input())
# for i in range(T):
#     x, y = map(int, sys.stdin.readline().split())    
#     Count(x, y)


# # 1978번
# N = int(input())
# A = map(int, input().split())
# CNT = 0
# for a in A:
#     cnt = 0
#     for i in range(1, a+1):
#         if a%i == 0:
#             cnt += 1
#     if cnt == 2:
#         CNT += 1
# print(CNT)



# #2581번
# M = int(input())
# N = int(input())
# A = []
# for a in range(M,N+1):
#     flag = 0
#     if a > 1:
#         for b in range(2,a):
#             if a%b == 0:
#                 flag = 1
#                 break
#         if flag == 0:
#             A.append(a)

# if len(A) != 0 :
#     print(sum(A))
#     print(min(A))
# else:
#     print(-1)



# # 11653번
# N = int(input())
# i = 2
# while True:
#     if N == 1:
#         break
#     if N < i:
#         break
#     if N%i == 0:
#         N /= i
#         print(i)
#     else:
#         i += 1
    


# # 1929번
# def primeNumber(M,N):
#     A = list(range(1,N+1))
#     for i in range(2,N-1):
#         if A[i-1] == 0:
#             continue
#         j = 2 * (i-1) +1
#         while j<= N-1:
#             A[j] = 0
#             j += i
#     return A
# M, N = map(int, input().split())
# A = primeNumber(M,N)
# A[0] = 0
# A = A[M-1:]
# for i in range(len(A)):
#     if A[i] != 0:
#         print(A[i])


# # 4948번                      ㅈㄴ 느림 나중에 수정할 것
# def primeNumber(N):
#     A = list(range(1,N+1))
#     for i in range(2,N-1):
#         if A[i-1] == 0:
#             continue
#         j = 2 * (i-1) +1
#         while j<= N-1:
#             A[j] = 0
#             j += i
#     A[0] = 0
#     return A
# while True:    
#     n = int(input())
#     if n == 0:
#         break
#     n2 = 2*n
#     A = primeNumber(n2)
#     A = A[n:]
#     print(len(A)-A.count(0))



# # 9020번
# # def primeNumber(N):
# #     A = list(range(1,N+1))
# #     for i in range(2,N-1):
# #         if A[i-1] == 0:
# #             continue
# #         j = 2 * (i-1) +1
# #         while j<= N-1:
# #             A[j] = 0
# #             j += i
# #     A[0] = 0
# #     return A

# # import time
# # start = time.time()

# # from math import sqrt
# # def primeNumber(N):
# #     A = []
# #     for n in range(2, N+1):
# #         flag = 0
# #         if n > 1:
# #             for i in range(2,int(sqrt(n))+1):
# #                 if n % i == 0:
# #                     flag = 1
# #                     break
# #             if flag == 0:
# #                 A.append(n)
# #     return str(A)
# # # T= int(input())
# # # for a in range(T):
# # for N in range(4, 10001):
# #     if N%2 == 0:
# #     # N = int(input())
# #         A = primeNumber(N)
# #         for i in range(int(N/2), N+1):
# #             if A.find(str(i)) != -1:
# #                 if A.find(str(N - i)) != -1:
# #                     B = [i, N-i]
# #                     B.sort()
# #                     break
# #         print(B[0], B[1])
# # print("time : ",time.time()-start)

# import sys
# def primeNumber(N):
    
#     A = list(range(1,N+1))
#     for i in range(2,N-1):
#         if A[i-1] == 0:
#             continue
#         j = 2 * (i-1) +1
#         while j<= N-1:
#             A[j] = 0
#             j += i
#     A[0] = 0
    
#     return A
# A = primeNumber(10000)
# A_ = A[:]

# T = int(input())
# for t in range(T):
#     N = int(sys.stdin.readline())
#     A = A_[:]
#     if A[int(N/2)-1] == 0: # N/2 가 소수가 아닐 때
#         A[int(N/2)-1] = int(N/2)
#         A.sort()
#         A.reverse()
#         Z = A.index(0)
#         A = A[:Z]
#         A.sort()
#         k = A.index(int(N/2)) + 1
#         while True:
#             try:
#                 if A.index(N - A[k]) != 0:
#                     B = [A[k], N - A[k]]
#                     B.sort()
#                     print(B[0], B[1])
#                     break
#             except:
#                 k+=1
#     else:
#         print(int(N/2), int(N/2))

# import sys

# T = int(sys.stdin.readline())

# demicial_list = [False, False] + [True]*9999
# a = int((10001**0.5)+1)
# for i in range(1, a):
#     if demicial_list[i] == True:
#         for j in range(2*i, 10001, i):
#             demicial_list[j] = False

# for i in range(T):
#     n = int(sys.stdin.readline())
#     a = n // 2
#     b = n // 2
#     while True:
#         if demicial_list[a] == True and demicial_list[b] == True:
#             print(a, b)
#             break
#         else:
#             a -= 1
#             b += 1




# 1085번
# import sys
# def Distance(x, y, w, h):
#     B =[]
#     if w - x <= x:
#         B.append(w-x)
#     else:
#         B.append(x)
#     if h - y <= y:
#         B.append(h - y)
#     else:
#         B.append(y)
#     B.sort()
#     return B[0]
# x, y, w, h = map(int, sys.stdin.readline().split())
# print(Distance(x, y, w, h))


# 3009번
# cnt = []
# cnt1 =[]
# cnt2 =[]
# for t in range(3):
#     a, b = map(int, input().split())
#     cnt1.append(a)
#     cnt2.append(b)
# for n1 in cnt1:
#     if cnt1.count(n1)%2 != 0:
#         cnt.append(n1) 
#         break
# for n2 in cnt2:
#     if cnt2.count(n2)%2 != 0:
#         cnt.append(n2)
#         break
# print(cnt[0],cnt[1])


# # 4153번
# import sys
# def IsRightTriangle(a,b,c):
#     A = [a, b, c]
#     A.sort()
#     if A[0]*A[0] + A[1]*A[1] == A[2]*A[2]:
#         return "right"
#     else:
#         return "wrong"
# while True:
#     a, b, c = map(int, sys.stdin.readline().split())
#     if abs(a)+abs(b)+abs(c) == 0:
#         break
#     print(IsRightTriangle(a, b, c))


# # 3053번
# from math import *
# R = int(input())
# print("{:.6f}".format(R*R*pi))
# print("{:.6f}".format(R*R*2))




# # 1002번
# import sys
# def Distance(x1, y1, x2, y2):
#     return ((x1-x2)**2 + (y1-y2)**2)**0.5

# T = int(input())
# for t in range(T):
#     x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
#     dis = Distance(x1, y1, x2, y2)
#     if dis == 0:
#         if r1 == r2:
#             print(-1)
#         else:
#             print(0)
#     else:
#         if dis == r1 + r2 or dis + r1 == r2 or dis +r2 == r1:
#             print(1)
#         elif dis > r1 + r2 or r2 > r1 + dis or r1 > r2 + dis:
#             print(0)
#         elif dis < r1 + r2:
#             print(2)
        

# # 10872번
# def Factorial_(n, fac =1):
#     if n == 0:
#         return print(fac)
#     else:
#         fac *= n
#         n -= 1
#         Factorial_(n, fac)

# Factorial_(int(input()))


# # 10870번
# def Fibonacci(n):
#     if n>=2:
#         return Fibonacci(n-1) + Fibonacci(n-2)
#     elif n == 1:
#         return 1
#     else:
#         return 0
# print(Fibonacci(int(input())))


# # 2447번
# import time
# from math import *
# start = time.time()
# def DrawStar(n):
#     if n>3:
#         b = []
#         for i in range(n):
#             if i < n//3:
#                 b.append(3 * DrawStar(n//3)[i])
#             elif n//3 <= i < n//3 * 2:
#                 b.append(DrawStar(n//3)[i-n//3] + n//3*' ' + DrawStar(n//3)[i-n//3])
#             else:
#                  b.append(3 * DrawStar(n//3)[i - n//3*2])
#         return b
#     else:
#         a = ['***', '* *', '***'] 
#         return a
# A = DrawStar(int(input()))
# for i in range(len(A)):
#     A.insert(2*i+1,'\n')
# for i in A:
#     print(i, end= "")
# print("time : ",time.time() - start)

# # 243,12초

# import time
# import sys
# from math import *
# start = time.time()
# def DrawStar(n):
#     if n>3:
#         N = n//3
#         b = []
#         a = DrawStar(N)
#         for i in range(n):
#             if i < N:
#                 b.append(3 * a[i])
#             elif N <= i < N * 2:
#                 b.append(a[i-N] + N * ' ' + a[i-N])
#             else:
#                  b.append(3 * a[i - N*2])
#         return b
#     else:
#         a = ['***', '* *', '***'] 
#         return a
# A = DrawStar(int(input()))
# for i in range(len(A)):
#     A.insert(2*i+1,'\n')
# for i in A:
#     # print(i, end= "")
#     sys.stdout.write(i)
# print("time : ",time.time() - start)
# # # 3초



# # 11729번
# def Log_1(log):
#     log = log.replace("3","x")
#     log = log.replace("2","3")
#     log = log.replace("x","2")
#     return log
# def Log_2(log):
#     log = log.replace("2","x")
#     log = log.replace("1","2")
#     log = log.replace("x","1")
#     return log


# def Hanoi(n):
#     if n>1:
#         log, cnt = Hanoi(n-1)
#         log1 = Log_1(log)
#         log2 = Log_2(log)
#         cnt = 2*cnt +1
#         log = log1 + "1 3\n" + log2
#         return log, cnt
#     else:
#         log = "1 3\n"
#         cnt = 1
#     return log, cnt

# log, cnt = Hanoi(int(input()))
# print(cnt)
# print(log)


# 1018번
# def Eight_Eight_Chess(color):
#     chess = []
#     if color == 'B':
#         for i in range(8):
#             if i%2:
#                 chess.append("WBWBWBWB")
#             else:
#                 chess.append("BWBWBWBW")
#     else:
#         for i in range(8):
#             if i%2:
#                 chess.append("WBWBWBWB")
#             else:
#                 chess.append("BWBWBWBW")
#     return chess

# import time

# start = time.time()
# import sys
# def Eight_Eight_Chess():
#     # white : T , Black : F
#     chess_W = [True, False] * 40 +[True]
#     chess_B = [False, True] * 40 +[False]
#     return chess_W, chess_B
    


# def Count_Diff_Color(Origin ,row, col):
#     Check_Array = []
#     cnt_w = 0
#     cnt_b = 0
#     chess_w , chess_b = Eight_Eight_Chess()
#     for i in range(row, row+8):
#         Check_Array.append(str(Origin[i])[col:col+8])
#     for i in range(8):
#         for j in range(8):
#             if chess_w[i+j]:
#                 if str(Check_Array[j])[i] == "B":
#                     cnt_w += 1
#             else:
#                 if str(Check_Array[j])[i] == "W":
#                     cnt_w += 1
#             if not chess_b[i+j]:
#                 if str(Check_Array[j])[i] == "W":
#                     cnt_b += 1
#             else:
#                 if str(Check_Array[j])[i] == "B":
#                     cnt_b += 1
#     return min(cnt_w, cnt_b)



# N, M = map(int, input().split())
# origin_chess = []
# cnt = []
# for _ in range(N):
#     origin_chess.append(sys.stdin.readline().rstrip())
# for n in range(N-7):
#     for m in range(M-7):
#         cnt.append(Count_Diff_Color(origin_chess, n, m))
# print(min(cnt))

# # print("time : ",time.time() - start)


