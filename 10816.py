import sys

input = sys.stdin.readline


user_have = []

dealer_have = []
from collections import Counter
for i in range(2):
    count = int(input())
    
    card_list = list(map(int,input().split()))
    if i == 0:
        user_have.extend(card_list)
        user_have = Counter(user_have)

    else:
        dealer_have.extend(card_list)
    

print(user_have)
print(dealer_have)





def check(x,y):
    result_list = []

    for i in y:
        result = x.get(i)
        if result != None:
            result_list.append(str(result))
        else:
            result_list.append(str(0))
    return print(' '.join(result_list))


check(user_have,dealer_have)