import sys
import numpy as np
input = sys.stdin.readline

A = int(input())

room_arr = np.zeros((5,5))
print(room_arr)
row = 0
column = 0
for i in range(A):
    B = str(input().strip())
    for j in range(len(B)):
        if B[j] == 'x':
            room_arr[i][j] = 1
print(room_arr)
        
for i in range(len(room_arr)):
    for j in range(len(room_arr[i])):
        if room_arr[j:j+2] == np.array([0,0]):
            row +=1
print(row)