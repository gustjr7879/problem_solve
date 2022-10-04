import sys

input = sys.stdin.readline

N,K = map(int,input().split())

num_list = []

num = str(input())

for i in range(N):
    num_list.append(int(num[i]))


while True:
    max_idx = num_list.index(max(num_list))

    if len(num_list) == N-K:
        break
    else:
        if max_idx == 0:#이때는 무조건 뒤에있으니까 계속 구할필요 없음
            min_val = min(num_list[max_idx+1:])
            num_list.remove(min_val)
        else:
            min_val = min(num_list[:max_idx])
            num_list.remove(min_val)
print(*num_list, sep='')