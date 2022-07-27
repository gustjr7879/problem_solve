# 1. gold
# 2. same gold -> sliver
# 3. same gold and sliver -> bronze

import sys
import numpy as np
input = sys.stdin.readline

A,B = map(int,input().split())

# A is num of country
# B is print country

country_list = []
medal_list = []
for i in range(A):
    input_list = list(map(int,input().split()))
    country_list.append(input_list[0])
    medal_list.append(input_list[1:])

dict_country = []
for i in range(len(country_list)):
    dict_country_dict = {country_list[i]:medal_list[i]}
    dict_country.append(dict_country_dict)

print(dict_country)
