import sys

input = sys.stdin.readline

num = int(input())
start, target = map(int,input().split())
num_edge = int(input())

graph_list = [[] for _ in range(num+1)]

for j in range(num_edge):
    parent , child = map(int,input().split())
    graph_list[parent].append(child)
    graph_list[child].append(parent)

check = [0]*(num+1)
from collections import deque

def bfs(root):
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        for i in graph_list[node]:
            if check[i] == 0:
                check[i] = check[node] + 1
                queue.append(i)

bfs(start)
if check[target] >0:
    print(check[target])
else:
    print(-1)

