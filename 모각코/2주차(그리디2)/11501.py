import sys

input = sys.stdin.readline

#주식 사기(1주)
#원하는 만큼 팔기(가지고 있는)
#아무것도 안하기

num = int(input())

for i in range(num):
    days = int(input())
    days_price = list(map(int,input().split()))
    account = 0
    max_price = days_price[-1]
    for j in range(days-2,-1,-1):
        if days_price[j]>max_price:
            max_price = days_price[j]
        else:
            account += max_price-days_price[j]
    print(account)