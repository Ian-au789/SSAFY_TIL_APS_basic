# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEvI_ZKa0wDFAVs&probBoxId=AZTP3wYKXqvHBIRD&type=USER&problemBoxTitle=%2802.17%29+Stack2-1&problemBoxCnt=5

import sys
sys.stdin = open("4875_input.txt")


def maze_clear(size, start, last, end):

    if start == end:
        return 1

    else:
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        for k in range(4):
            next_step = [start[0] + di[k], start[1] + dj[k]]
            if next_step != last:
                if 0 <= next_step[0] < size and 0 <= next_step[1] < size:
                    if maze[next_step[0]][next_step[1]] == 0:
                        return maze_clear(size, next_step, start, end)

        else:
            return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        input_list = list(map(int, input()))
        maze.append(input_list)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                maze_in = [i, j]
            if maze[i][j] == 3:
                maze_out = [i, j]

    print(f"#{t} {maze_clear(N, maze_in, maze_in, maze_out)}")
