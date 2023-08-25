#dp란? -> 하나의 큰 문제를 여러 작은 문제로 나눠서 풀고 결과를 저장해서 꺼내서 쓰는 방식
#기억하며 풀기.. 느낌
#재귀를 통해서 풀때 반복되는 연산때문에 귀찮아지는 것 방지
#dp가 사용가능하려면 동일한 작은문제들 즉, 겹치는 문제가 존재할 때 사용가능하다

#계단을 밟으면 점수를 얻음
#한번에 한계단, 혹은 두계단을 오를수있음 
#연속으로 세개를 오를 수 없음
#마지막 도착 계단은 반드시 밟아야함

import sys

st_num = int(sys.stdin.readline())

score_list = []
for i in range(st_num):
    score = int(sys.stdin.readline())
    score_list.append(score)
#score_list = score_list[::-1]

dp = [0 for i in range(st_num)] 
#dp[0] = score_list[0]
if len(score_list)<=2:
    print(sum(score_list))
else:
    dp[0] = score_list[0]
    dp[1] = dp[0]+score_list[1]
    for i in range(2,len(score_list)):
        dp[i] = max(dp[i-3]+score_list[i-1]+score_list[i],dp[i-2]+score_list[i])
    print(dp[-1])