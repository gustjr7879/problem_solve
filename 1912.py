import sys

num = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))
#연속된 수의 합에서 가장 큰 값
#-기준으로 묶기
s = 0
s_list = []
for i in num_list:
    if i > 0:
        s+=i
    else:
        s_list.append(s)
        s=i
        s_list.append(s)
        s = 0


max_v = 0

for i in range(0,len(s_list)):
    dp = [0 for j in range(i,len(s_list))]
    dp[0] = s_list[i]
    dp[1] = s_list[i] + dp[0]
    for j in range(i+2, len(s_list)):
        dp[j] = s_list[j] + dp[j-1]
        print(dp[j])
    print(dp)