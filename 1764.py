import sys

not_li, not_see = map(int,input().split())

not_li_list = []
not_see_list = []

for i in range(not_li):
    name = str(input())
    not_li_list.append(name)


for j in range(not_see):
    name = str(input())
    not_see_list.append(name)


def intersection(list1,list2):
    intersection = list(set(list1)&set(list2))
    return intersection

result = sorted(intersection(not_li_list,not_see_list))
print(len(result))
for i in range(len(result)):
    print(result[i])