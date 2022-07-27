import sys

input = sys.stdin.readline


A = int(input())


num_list =[]
for i in range(A):
    a,b = map(int,input().split())
    num_list.append([a,b])


def GDC(x,y):
    while y:
        x,y = y,x%y
    return x

def LCM(x,y):
    result = (x*y)//GDC(x,y)
    return print(result)

for i in num_list:
    LCM(i[0],i[1])

    