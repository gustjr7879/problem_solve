import sys

input = sys.stdin.readline

#only use 2won / 5won 
#minimum coin

#money is n
#how many coin minimum?

#input 1 = 13 5 + 2*4
#input 2 = 14 5*2 + 2*2
#cant : 1,3

coin = int(input())

num = coin%5

count = 0

if coin == 1 or coin == 3:
    print(-1)
    exit(0)
elif num%2 == 0:
    print(coin//5 + num//2)
    exit(0)
else:
    print((coin//5)-1 + (num+5)//2)
    exit(0)