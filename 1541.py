li = input().split('-')
sum = 0
for i in li[0].split('+'):
    sum += int(i)
for i in li[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)