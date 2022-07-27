import sys

input = sys.stdin.readline

num, K = map(int,input().split())


from collections import deque

test_list = deque([])
for i in range(1,num+1):
    test_list.append(i)

result = []

while len(test_list) > 0:

    test_list.rotate(-(K-1))
    result.append(test_list[0])
    test_list.remove(test_list[0])

str_result=list(map(str, result))
print('<'+', '.join(str_result)+'>')