import sys

input = sys.stdin.readline

num_test = int(input())
# 규칙 : A[n] = A[n-3] + A[n-2] + A[n-1}


for i in range(num_test):
    N = int(input())
    if N == 1:
        print(1)
    elif N ==2 :
        print(2)
    elif N == 3 :
        print(4)
    else:
        sum_list = [1,2,4]
        i = 0
        while len(sum_list)<N:
            sum_list.append(sum(sum_list[i:i+3]))
            i+=1
        print(sum_list[-1])
