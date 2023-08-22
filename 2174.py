import sys

A,B = map(int,sys.stdin.readline().split())
N,M = map(int,sys.stdin.readline().split())
robot_list = []
for i in range(N):
    robot1 = list(sys.stdin.readline().split())
    robot_list.append(robot1)

for j in range(M):
    act = list(sys.stdin.readline().split())
    #act[0] = robot num [1] 방향 [2] 반복횟수
    robot_list[int(act[0])]


#행렬 생성 
#robot location불러와서 행렬에 표시 -> act진행 -> robot location업데이트(행렬에)
#충돌여부 확인
#없다면 다음 act진행...
#끝나면 OK출력