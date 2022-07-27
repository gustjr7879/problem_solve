import sys

input = sys.stdin.readline

num = int(input())


test_list = list(map(int,input().split()))

result_list = sorted(set(test_list))

print(*result_list)

