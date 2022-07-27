import sys

input = sys.stdin.readline


def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x

def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result

A,B = map(int,input().split())

print(GCD(A,B))
print(LCM(A,B))