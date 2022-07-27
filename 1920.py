# time over code
'''
import sys

inpput = sys.stdin.readline

A = int(input())

check_list = list(map(int,input().split()))

B = int(input())

in_list = list(map(int,input().split()))
def check(list1,list2):
    for i in list2:
        if i in list1:
            print(1)
        else:
            print(0)


print(check(check_list,in_list))
'''

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

A = int(input())

check_list = list(map(int,input().split()))
check_list = sorted(check_list)


def binary_search(list1,target):
    

    left = 0
    right = len(check_list)-1
    
    while left <= right:
        middle_idx = (left+right)//2
        middle = list1[middle_idx]

        if target == middle:
            return 1
        
        elif middle > target:
            right = middle_idx - 1
            #middle_idx = (middle_idx - 1)//2
            
        elif middle < target:
            left = middle_idx + 1
            #middle_idx = (left + right)//2
        
    return 0 
B = int(input())

in_list = list(map(int,input().split()))


for i in in_list:
    print(binary_search(check_list,i))
