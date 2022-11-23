import sys, heapq
input = sys.stdin.readline

n = int(input())

ant_E_list = []
hole = [[] for _ in range(n)]
d = [100000000000000000] * n

path = [[] for _ in range(n)]
result = [1] # 1 ant only 1
for i in range(n):
    E = int(input())
    ant_E_list.append(E)


for u in range(n-1):        
    hole1, hole2, holeE = map(int,input().split())
    hole[hole1-1].append((hole2-1,holeE))
    hole[hole2-1].append((hole1-1,holeE))

result = [1]

def dijstra(n):
    d[n] = 0
    min_queue = []
    min_queue.append((d[n],n))
    while len(min_queue) !=0:
        dist = min_queue[0][0]
        cur = min_queue[0][1]
        heapq.heappop(min_queue)
        if d[cur] < dist:
            continue
        for i in range(len(hole[cur])):
            next = hole[cur][i][0]
            next_dist = hole[cur][i][1] + dist
            if next_dist < d[next]:
                d[next] = next_dist
                path[next].append(cur)
                heapq.heappush(min_queue,(next_dist,next))

dijstra(0)
for i in range(1,n):
    for j in hole[i]:
        if j[0] == path[i][0]:
            path[i].append(j[1])

path[0] = [0,0] # 

for i in range(1,n):
    E = ant_E_list[i]
    rout = i
    while True:
        E -= path[rout][1]
        if E < 0:
            result.append(rout + 1)
            break
        elif rout == 0:
            result.append(rout + 1)
            break
        rout = path[rout][0]

for i in result:
    print(i)