import sys

lenlist_1, lenlist_2 = map(int,input().split())

list_1 = list(map(int,input().split()))

list_2 = list(map(int,input().split()))

def sys_diff(list1,list2):
    result1 = list(set(list1)^set(list2))
    

    return result1

a = sys_diff(list_1,list_2)

print(len(a))
