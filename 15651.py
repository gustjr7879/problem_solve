import sys

input = sys.stdin.readline

N,M = map(int,input().split())

from itertools import product

permu = product(range(1,N+1),repeat=M)


for i in permu:
    print(' '.join(map(str,i)))