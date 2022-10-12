import sys

input = sys.stdin.readline

#dp 2차원 dp 
#오른쪽, 아래, 오른쪽 아래 대각선으로만 움직일 수 있음
#1,1에서 3,2로 이동한다는 것은
#3,2의 왼쪽 2,2
#3,2의 위 3,1
#3,2 의 왼쪽 위 2,1에 대한 모든 경우의 수를 구하면 된다.

n,m = map(int,input().split())

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

dp[1][1] = 1

for i in range(1,n+1):
    for j in range(1,m+1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

print(dp[n][m]%1000000007)