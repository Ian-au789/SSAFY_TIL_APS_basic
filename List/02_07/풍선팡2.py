# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AYYlGU56XOkDFARc&probBoxId=AZTP3wYKXqXHBIRD&type=USER&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

import sys
sys.stdin = open("input1.txt", "r")


def paper_powder(row, column, matrix):
    di = [0, 1, 0, -1, 0]
    dj = [0, 0, 1, 0, -1]                      # 오늘 배운 델타 탐색
    max_powder = 0

    for i in range(row):
        for j in range(column):
            sum_powder = 0
            for k in range(5):
                ci = i + di[k]
                cj = j + dj[k]

                if 0 <= ci < row and 0 <= cj < column:    # 상하좌우 좌표가 범위 내에 있는 경우만
                    sum_powder += matrix[ci][cj]          # 꽃가루 더하기

            if max_powder < sum_powder:                   # 최댓값 갱신
                max_powder = sum_powder

    return max_powder


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    input_matrix = []

    for n in range(N):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{t} {paper_powder(N, M, input_matrix)}")
