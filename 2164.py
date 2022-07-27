#queue

import sys
from collections import deque

input = sys.stdin.readline

A = int(input())

test_list = []

for i in range(A):
    test_list.append(i+1)

test_list = deque(test_list)
while len(test_list) >0:
    if len(test_list)>1:
        
        test_list.popleft()
        test_list.rotate(-1)
    else: 
        break
    
print(test_list[0])