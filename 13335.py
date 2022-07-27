import sys

input = sys.stdin.readline

num_truck, len_bridge, max_weight = map(int,input().strip().split())


truck_list = list(map(int,input().strip().split()))

on_the_bridge = [0]*len_bridge
t = 0
while True:
    on_the_bridge.pop(0)
    weight = sum(on_the_bridge)
    
    
    if truck_list:
        if weight + truck_list[0] <= max_weight:
            
            on_the_bridge.append(truck_list[0])
            truck_list.remove(truck_list[0])
            

        else:
            on_the_bridge.append(0)
    t+=1
    if not on_the_bridge:
        break
print(t)