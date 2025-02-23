# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14wL9KAGkCFAYD&probBoxId=AZTP3wYKXq7HBIRD&type=PROBLEM&problemBoxTitle=%2802.20%29+Queue-2&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")

def maze_clear(maze_in, maze_out):
    queue = [maze_in]

    di = [1, 0, -1, 0]  # 상하좌우 델타 탐색
    dj = [0, 1, 0, -1]
    while len(queue) > 0:
        for k in range(4):
            next_step = [queue[0][0] + di[k], queue[0][1] + dj[k]]  # 다음에 이동할 곳
            if next_step == maze_out:
                return 1

            if maze[next_step[0]][next_step[1]] == 0:
                maze[next_step[0]][next_step[1]] = 1                # 이미 지나간 곳은 1로 표시
                queue.append(next_step)

        else:
            queue.pop(0)                                            # 다음에 이동할 곳 탐색이 끝나면 기존 위치 제거

    return 0


for _ in range(10):
    t = int(input())
    maze = []
    for _ in range(100):
        input_list = list(map(int, input()))
        maze.append(input_list)

    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                maze_in = [i, j]
            if maze[i][j] == 3:
                maze_out = [i, j]

    print(f"#{t} {maze_clear(maze_in, maze_out)}")
