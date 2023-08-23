import sys

num,max = map(int,sys.stdin.readline().split())

weight_list = []
value_list = []
for i in range(num):
    weight,value = map(int,sys.stdin.readline().split())
    weight_list.append(weight)
    value_list.append(value)
kv_dict= dict(zip(weight_list,value_list))
total_value_list = []
from itertools import combinations
total_com_list = []
for i in range(1,num+1):
    com_list = list(combinations(weight_list,i))
    for j in com_list:
        if sum(j) <= max:
            total_com_list.append(j)
max_val = 0
for i in total_com_list:
    val = 0
    for j in i:
        val += kv_dict.get(j)
    if i == 0:
        max_val = val
    else:
        if val > max_val:
            max_val = val   
print(max_val)