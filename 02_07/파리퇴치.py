# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PzOCKAigDFAUq&probBoxId=AZTP3wYKXqXHBIRD&type=PROBLEM&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

import sys
sys.stdin = open("input.txt", "r")


def catch_fly(area, kill, matrix):
    search = area-kill+1                            # 맨 왼쪽 위 꼭지점 기준으로 해서 파리채가 영역을 벗어나지 않는 탐색 범위
    max_fly = 0

    for i in range(search):
        for j in range(search):
            dead_fly = 0
            for di in range(kill):                  # 기준점에서 파리채 범위 내 항목 전부 탐색
                for dj in range(kill):
                    dead_fly += matrix[i+di][j+dj]

            if max_fly < dead_fly:                  # 최댓값 갱신
                max_fly = dead_fly

    return max_fly


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    input_matrix = []

    for n in range(N):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{t} {catch_fly(N, M, input_matrix)}")
