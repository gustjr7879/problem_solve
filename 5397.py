import sys
input = sys.stdin.readline

A = int(input())
pass_list = []
for i in range(A):
    pass_list.append(str(input()))



for u in pass_list:
    result = []
    point = 0
    for z in range(len(u)):
        if u[z] == '<' or u[z] == '>' or u[z] == '-':
            if len(result) == 0:
                pass
            elif len(result) > 0:
                if u[z] == '<':
                    point -=1
                elif u[z] == '>':
                    point +=1
                else:
                    result.pop(point-1)
                    point -=1
        else:
            if point > len(result):
                result.append(u[z])
                point = len(result)
            elif point <= len(result):
                result.insert(point,u[z])
                point +=1
    str = ''.join(result[:len(result)-1])
    print(str)