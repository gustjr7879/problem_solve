import sys

input = sys.stdin.readline



n,m,circle = map(int,input().split())

dp = [[0] * m for _ in range(n)]


if circle == 0:
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[n-1][m-1])
else:
    #circle 좌표 계산
    circle_n = (circle-1)//m
    circle_m = (circle-1)%m
    for i in range(circle_n+1):
        for j in range(circle_m+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp_1 = dp[circle_n][circle_m]

    new_n = n-circle_n
    new_m = m-circle_m
    dp = [[0] * new_m for _ in range(new_n)]

    for i in range(new_n):
        for j in range(new_m):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp_2 = dp[new_n-1][new_m-1]
    print(dp_1*dp_2)