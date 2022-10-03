import sys

input = sys.stdin.readline

first = str(input())
second = str(input())
first = first[:len(first)-1]
second = second[:len(second)-1]
#second 맨 뒤가 A일 때 
#second 에서 a 뺌
#맨 뒤가 b일 때
#b를 빼고 리버스해줌
#둘의 길이가 같아졌을 때 같은지 파악하기





while True:
    if len(second) == len(first):
        break
    else:
        if second[-1] == 'A':
            second = second[:len(second)-1]
        elif second[-1] == 'B':
            second = second[:len(second)-1]
            second = second[::-1]
if first == second:
    print(1)
else:
    print(0)
