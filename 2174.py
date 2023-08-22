import sys

A,B = map(int,sys.stdin.readline().split())
N,M = map(int,sys.stdin.readline().split())
robot_list = []
for i in range(N):
    robot1 = list(sys.stdin.readline().split())
    if robot1[2] == 'N':
        robot1[2] = 0
    elif robot1[2] == 'E':
        robot1[2] = 1
    elif robot1[2] == 'S':
        robot1[2] = 2
    elif robot1[2] == 'W':
        robot1[2] = 3    
    robot_list.append(robot1)
#north = 0
#east = 1
#south = 2
#west = 3


for j in range(M):
    act = list(sys.stdin.readline().split())
    #act[0] = robot num [1] 방향 [2] 반복횟수
    if act[1] == 'L':
        robot_list[int(act[0])][2] -= int(act[2])
    elif act[1] == 'R':
        robot_list[int(act[0])][2] += int(act[2])
    else:
        if robot_list[int(act[0])][2] == 0:
            robot_list[int(act[0])][1] += int(act[2])
            if robot_list[int(act[0])][1] <= 0 or robot_list[int(act[0])][1] > B:
                print('Robot {} crashes into the wall',int(act[0]))
                exit(0)
            for __ in range(N):
                if __ != robot_list[int(act[0])][1] and robot_list[int(act[0])][1] == robot_list[int(act[0])][1]:
                    print('Robot {} crashes into robot {}'.format(int(act[0]), __))
                    exit(0)
        elif robot_list[int(act[0])][2] == 1:
            robot_list[int(act[0])][0] += int(act[2])
            if robot_list[int(act[0])][1] <= 0 or robot_list[int(act[0])][1] > A:
                print('Robot {} crashes into the wall',int(act[0]))
                exit(0)
            for __ in range(N):
                if __ != robot_list[int(act[0])][1] and robot_list[int(act[0])][1] == robot_list[int(act[0])][1]:
                    print('Robot {} crashes into robot {}'.format(int(act[0]), __))
                    exit(0)
        elif robot_list[int(act[0])][2] == 2:
            robot_list[int(act[0])][1] -= int(act[2])
            if robot_list[int(act[0])][1] <= 0 or robot_list[int(act[0])][1] > B:
                print('Robot {} crashes into the wall',int(act[0]))
                exit(0)
            for __ in range(N):
                if __ != robot_list[int(act[0])][1] and robot_list[int(act[0])][1] == robot_list[int(act[0])][1]:
                    print('Robot {} crashes into robot {}'.format(int(act[0]), __))
                    exit(0)
        elif robot_list[int(act[0])][2] == 3:
            robot_list[int(act[0])][0] -= int(act[2])
            if robot_list[int(act[0])][1] <= 0 or robot_list[int(act[0])][1] > A:
                print('Robot {} crashes into the wall',int(act[0]))
                exit(0)
            for __ in range(N):
                if __ != robot_list[int(act[0])][1] and robot_list[int(act[0])][1] == robot_list[int(act[0])][1]:
                    print('Robot {} crashes into robot {}'.format(int(act[0]), __))
                    exit(0)
print('OK')
