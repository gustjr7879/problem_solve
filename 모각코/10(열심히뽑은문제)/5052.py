import sys

input = sys.stdin.readline

test_case = int(input())
# number 중에서 가장 짧은것 -> 비교 / 다음 짧은 것 -> 비교 식으로
for i in range(test_case):
    number_num = int(input())
    number_list = []
    for j in range(number_num):
        number = str(input())
        number_len = len(number)
        number_list.append(number[:number_len-1])
    number_list = sorted(number_list)
    cnt = 0
    for z in range(number_num-1):
        check = len(number_list[z])
        if number_list[z] == number_list[z+1][:check]:
            cnt +=1
            break
    if cnt != 0:
        print('NO')
    else:
        print('YES')