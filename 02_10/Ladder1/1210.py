# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14ABYKADACFAYh&probBoxId=AZTP3wYKXqbHBIRD&type=PROBLEM&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")

'''
사다리 타기
1. 출발점이 있는 열은 1이 쭉 그어져있다.
2. 1을 따라 내려가다가 왼쪽이나 오른쪽에 1이 있으면 방향 전환
3. 옆으로 이동하다가 해당 방향의 막다른 길을 마주치면 다시 하강 시작
4. 99번째 행에 도착했을 때 그 항목의 값이 2라면 당첨
'''


def ladder(matrix):
    start_point = []

    for point in range(100):
        if matrix[0][point] == 1:                           # 1이 저장된 사다리 시작점 확인
            start_point.append(point)

    for number in start_point:                              # 시작점 하나씩 사다리 출발
        idx_x = number                                      # 좌표 [idx_y][idx_x] 초깃값 설정
        idx_y = 0

        while idx_y < 99:
            if 0 <= idx_x - 1 < 100:                        # 인덱스 범위 확인
                if matrix[idx_y][idx_x - 1] == 1:           # 왼쪽에 사다리가 이어졌나 확인
                    idx_x -= 1
                    while matrix[idx_y + 1][idx_x] == 0:    # 아래로 내려가는 길이 나타날 때 까지 왼쪽으로 이동
                        idx_x -= 1
                    idx_y += 1                              # 아래로 내려가는 길이 생기면 방향 전환 후 다시 주변 체크
                    continue

            if 0 <= idx_x + 1 < 100:                        # 인덱스 범위 확인
                if matrix[idx_y][idx_x + 1] == 1:           # 오른쪽에 사다리가 이어졌나 확인
                    idx_x += 1
                    while matrix[idx_y + 1][idx_x] == 0:    # 아래로 내려가는 길이 나타날 때 까지 오른쪽으로 이동
                        idx_x += 1
                    idx_y += 1                              # 아래로 내려가는 길이 생기면 방향 전환 후 다시 주변 체크
                    continue

            idx_y += 1                                      # 그 외에 계속 하강

        if matrix[idx_y][idx_x] == 2:
            return number


for t in range(10):
    N = int(input())
    input_matrix = []
    for n in range(100):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{N} {ladder(input_matrix)}")