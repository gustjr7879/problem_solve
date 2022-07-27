#N and M

# 1. solve python itertools / permutations 
# 2. solve python using dfs

# 1 solve
'''
from itertools import permutations

import sys

input = sys.stdin.readline

N,M = map(int,input().split())

P = permutations(range(1,N+1),M)

for i in P:
    print(' '.join(map(str,i)))
'''

# 2 solve

import sys

input = sys.stdin.readline

N,M = map(int,input().split())

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))

    for i in range(1,N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

print(dfs())