from collections import deque
import sys

input = sys.stdin.readline


def baek_11866(num_list,num_delete):
    result_list = []
    test_list = []
    for i in range(num_list):
        test_list.append(i+1)
    while len(test_list)>num_delete-1:
        test_list = deque(test_list)
        result_list.append(test_list[num_delete-1])
        test_list.remove(test_list[num_delete-1])
        test_list.rotate(3)
    if num_delete%2 ==0:
        result_list.append(test_list.pop())
        result_list.append(test_list.pop())
    else:
        result_list.append(test_list.popleft())
        result_list.append(test_list.popleft())
    
    return result_list

A = list(map(int,input().split()))
num_list = A[0]
num_delete = A[1]
result = baek_11866(num_list,num_delete)

for i in range(len(result)):
    if i == 0:
        print('<{},'.format(result[i]), end=' ')
    elif i < (len(result)-1):
        print('{},'.format(result[i]), end=' ')
    else:
        print('{}>'.format(result[i]), end=' ')