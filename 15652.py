import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

num, sel_num = map(int,input().split())

num_list = []

for i in range(num):
    num_list.append(str(i+1))
# num_list 1,2,3...

result_str = ''.join(num_list)

#result_str is 123


result = combinations_with_replacement(result_str,sel_num)

for i in result:
    print(' '.join(map(str,i)))