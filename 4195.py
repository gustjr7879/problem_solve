import sys

input = sys.stdin.readline

A = int(input())
result = []
for i in range(A):
    B = int(input())
    friend_list = []
    num_friend = []
    for j in range(B):
        

        id1 , id2 = map(str,input().strip().split())
        if len(friend_list) == 0:
            friend_list.append(id1)
            friend_list.append(id2)
            num_friend.append(2)
        elif id1 in friend_list and id2 not in friend_list:
            friend_list.append(id2)
            num_friend.append(num_friend[j-1]+1)
        elif id1 not in friend_list and id2 not in friend_list:
            friend_list.append(id1)
            friend_list.append(id2)
            num_friend.append(2)
        else :
            num_friend.append(len(friend_list))
        result.append(num_friend[j])

for n in result:
    print(n)


