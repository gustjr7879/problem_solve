# N and M (2)

# combina....
# solve 1

'''
from itertools import combinations

import sys

input = sys.stdin.readline

N,M = map(int,input().split())

combi = combinations(range(1,N+1),M)


for i in combi:
    print(' '.join(map(str,i)))
'''

#solve 2

import sys

input = sys.stdin.readline

N,M = map(int,input().split())

s = []
def dfs(start):
    if len(s) == M:
        print(' '.join(map(str,s)))
    
    for i in range(start,N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

print(dfs(1))