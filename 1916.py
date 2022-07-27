#dijkstra

import sys

input = sys.stdin.readline

import heapq

A = int(input())

B = int(input())
city_dict = dict()
cost_dict = dict()
for i in range(B):
    start, end, cost = map(int,input().strip().split())
    cost_dict[end] = cost
    city_dict[start] = cost_dict[end]
    print(cost_dict)
    print(city_dict)
print(city_dict)