import sys

input = sys.stdin.readline

num_ = int(input())

num_list = list(map(int,input().split()))
cnt = 0
result_list = []
for i in range(num_+1):
    if i >=3:

        test_list = num_list[:i]
        beforecnt = cnt
        for j in range(len(test_list)-1):
            for u in range(j+1,len(test_list)-1):
                if test_list[j]+test_list[u] == test_list[-1]:
                    result_list.append(test_list[-1])
                    cnt += 1
                    break
            if  cnt != beforecnt:
                break    

print(cnt)