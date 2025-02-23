# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14vXUqAGMCFAYD&probBoxId=AZTP3wYKXq7HBIRD&type=PROBLEM&problemBoxTitle=%2802.20%29+Queue-2&problemBoxCnt=5&&&&&&

import sys
sys.stdin = open("input (1).txt")


def maze_clear(size, start, last, end):

    if start == end:                                                        # 원하는 목적지에 도착하면 1 반환
        return 1

    else:
        di = [1, 0, -1, 0]                                                  # 상하좌우 델타 탐색
        dj = [0, 1, 0, -1]
        for k in range(4):
            next_step = [start[0] + di[k], start[1] + dj[k]]                # 다음에 이동할 곳
            if next_step != last:                                           # 방금 전에 있던 곳 아니고
                if 0 <= next_step[0] < size and 0 <= next_step[1] < size:   # 2차원 배열 안에 있으며
                    if maze[next_step[0]][next_step[1]] != 1:               # 막혀 있지 않으면
                        if maze_clear(size, next_step, start, end) == 1:    # 해당 장소에 이동하고 함수 재귀 호출
                            return 1

        else:
            return 0                                                        # 더 이상 이동할 곳이 없으면 0 반환


for _ in range(10):
    t = int(input())
    maze = []
    for _ in range(16):
        input_list = list(map(int, input()))
        maze.append(input_list)

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                maze_in = [i, j]
            if maze[i][j] == 3:
                maze_out = [i, j]

    print(f"{t} {maze_clear(16, maze_in, maze_in, maze_out)}")
