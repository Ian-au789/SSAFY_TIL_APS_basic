# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZFODRmquDYDFAVs&probBoxId=AZTP3wYKXq7HBIRD&type=USER&problemBoxTitle=%2802.20%29+Queue-2&problemBoxCnt=5

import sys
sys.stdin = open("5105_input.txt")


def fast_clear(maze_in, maze_out):
    global N
    queue = [maze_in]
    level = [1]
    check = 0
    cnt = 0


    di = [1, 0, -1, 0]  # 상하좌우 델타 탐색
    dj = [0, 1, 0, -1]
    while len(queue) > 0:
        for k in range(4):
            next_step = [queue[0][0] + di[k], queue[0][1] + dj[k]]      # 다음에 이동할 곳

            if next_step == maze_out:
                return len(level) - 1

            if 0 <= next_step[0] <N and 0 <= next_step[1] < N:
                if maze[next_step[0]][next_step[1]] == 0:
                    maze[next_step[0]][next_step[1]] = 1                # 이미 지나간 곳은 1로 표시
                    queue.append(next_step)
                    cnt += 1                                            # 다음 레벨의 노드 개수 카운트

        else:
            queue.pop(0)                                            # 다음에 이동할 곳 탐색이 끝나면 기존 위치 제거
            check += 1

            if check == level[len(level) - 1]:                      # 이번 레벨의 노드 개수 만큼 탐색 완료했으면
                check = 0
                level.append(cnt)                                   # 해당 변수들 초기화 및 다음 레벨의 노드 개수 저장
                cnt = 0

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

    print(f"#{t} {fast_clear(maze_in, maze_out)}")
