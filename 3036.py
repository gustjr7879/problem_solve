import sys
import fractions
input = sys.stdin.readline

# circle 2pi r

num_circle = int(input())


circle_list = list(map(int,input().split()))

num_circle = len(circle_list)

first_circle = circle_list[0]

test_list = []
for i in range(1,num_circle):
    test_list.append(fractions.Fraction(first_circle, circle_list[i]))


for j in range(len(test_list)):
    result_list = []
    result_list.append(str(test_list[j].numerator))
    result_list.append(str(test_list[j].denominator))
    print('/'.join(result_list))

