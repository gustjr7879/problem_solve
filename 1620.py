import sys

input = sys.stdin.readline

iter_num , question = map(int,input().split())


pocket_list = []

for i in range(iter_num):
    pocketmon = str(input())
    pocket_list.append(pocketmon)

result_list = []
for j in range(question):
    question_q = input()
    result_list.append(question_q)

for n in range(len(result_list)):
    if result_list[n] is int:
        print(pocket_list[result_list[n]])
    else:
        for j in range(len(pocket_list)):
            if pocket_list[j] == result_list[n]:
                print(j)