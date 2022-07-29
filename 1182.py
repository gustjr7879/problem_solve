import sys

input = sys.stdin.readline


num, sum_sel = map(int,input().split())
# 5 0

num_list = list(map(int,input().split()))
# -7 -3 -2 5 8

from itertools import combinations
result = 0
for i in range(1,num+1):

    sum_sel_num = combinations(num_list,i)
    for j in sum_sel_num:
        sum_ = sum(j)
        if sum_ == sum_sel:
            result +=1
print(result)
    