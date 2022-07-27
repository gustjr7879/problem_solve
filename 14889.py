import sys

input = sys.stdin.readline

num = int(input())


adj_mat = []
num_list = []
for i in range(num):
    adj_mat.append(list(map(int,input().split())))
    num_list.append(i)
#num%2 == 0
from itertools import combinations

sum_list = []
for i in combinations(num_list,2):
    sum = adj_mat[i[0]][i[1]] + adj_mat[i[1]][i[0]]
    sum_list.append(sum)

result_list = []
for j in combinations(sum_list,2):
    result = abs(j[0] - j[1])
    result_list.append(result)

print(min(result_list))