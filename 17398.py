import sys

input = sys.stdin.readline

#union find connected component

import networkx as nx
import networkx.utils

num_node, num_edge, num_split = map(int,input().split())

edge_list = []
check_list = []
node_list = [i for i in range(1,num_node+1)]
for i in range(num_edge):
    edge = list(map(int,input().split()))
    edge_list.append(edge)
    check_list.append(edge)
result = 0

for j in range(num_split):

    point = int(input())
    
    
    check_list.remove(edge_list[point-1])
uni = networkx.utils.UnionFind(node_list)
for a,b in check_list:
    uni.union(a,b)
uni = sorted(map(sorted,uni.to_sets()))
for i in uni:
    if len(i) != 1:
        result += pow(len(i),2)
    else:
        result += 0.5
print(int(result))