import sys

input = sys.stdin.readline

#N+1 I N O -> Pn

#slide window

N = int(input())
len_M = int(input())
M = list(map(str,input()))

M = M[:len_M]

i = 1
cnt = 0
result = 0
while i < len_M-1:
    if M[i-1] == 'I' and M[i] == 'O' and  M[i+1] == 'I':
        cnt +=1 
        if cnt == N:
            cnt -= 1
            result += 1
        i += 1
    else:
        cnt = 0
    i += 1
print(result)
