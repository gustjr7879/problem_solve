#https://www.acmicpc.net/problem/14888

import sys

input = sys.stdin.readline()
num_list = list(map(int,sys.stdin.readline().split()))
oper_list = list(map(int,sys.stdin.readline().split())) # 0 plus 1 minus 2 multi 3 div
new_oper_list = []
cnt = 0
for i in range(len(oper_list)):
    
    for j in range(oper_list[i]):
        new_oper_list.append(cnt)
    cnt += 1
from itertools import combinations,permutations

perm = permutations(new_oper_list,len(new_oper_list))


perm = list(perm)
#print(perm)
#calculation
result_list = []

for i in perm:
    if list(i)[0] == 0:
        result = num_list[0] + num_list[1]
    elif list(i)[0] == 1:
        result = num_list[0] - num_list[1]
    elif list(i)[0] == 2:
        result = num_list[0] * num_list[1]
    elif list(i)[0]==3:
        result = int(num_list[0] / num_list[1])
    for j in range(1, len(list(i))):
        if list(i)[j] == 0:
            result += num_list[j+1]
        elif list(i)[j] == 1:
            result -= num_list[j+1]
        elif list(i)[j] == 2:
            result *= num_list[j+1]
        elif list(i)[j]==3:
            result = int(result / num_list[j+1])
    result_list.append(result)
max_re = max(result_list)
min_re = min(result_list)
#print(result_list)
print(max_re)
print(min_re)