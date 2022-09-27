import sys

input = sys.stdin.readline

num = int(input())

if num == 0:
    print(0)
else:
    result = []
    while num != 0:
        if num%(-2) == 0:
            result.append('0')
            num = num//(-2)
        else:
            result.append('1')
            num = num//(-2) + 1
    print(''.join(reversed(result)))