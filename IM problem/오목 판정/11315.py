# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXaSUPYqPYMDFASQ&probBoxId=AZT4yWiKS8vHBIOK&type=PROBLEM&problemBoxTitle=IM+%EB%8C%80%EB%B9%84%ED%95%98%EC%9E%90%21&problemBoxCnt=8

import sys
sys.stdin = open("sample_input.txt")


def five_in_row(size, matrix):
    # 가로 탐색
    for _ in range(2):
        for row in matrix:
            for k in range(size - 4):
                if row[k:k+5] == ["o", "o", "o", "o", "o"]:
                    return "YES"

        # 전치행렬로 행과 열 바꾸고 세로 탐색
        for i in range(size):
            for j in range(size):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 대각선 탐색 (오른쪽 아래 방향)
    for m in range(size - 4):
        for n in range(size - 4):

            check_diagonal = []
            for d in range(5):
                check_diagonal.append(matrix[m + d][n + d])

            if check_diagonal == ["o", "o", "o", "o", "o"]:
                return "YES"

    # 대각선 탐색 (왼쪽 아래 방향)
    for m in range(size - 4):
        for n in range(size-1, 3, -1):

            check_diagonal = []
            for d in range(5):
                check_diagonal.append(matrix[m+d][n-d])

            if check_diagonal == ["o", "o", "o", "o", "o"]:
                return "YES"

    return "NO"


T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_matrix = []
    for _ in range(N):
        input_list = list(map(str, input()))
        input_matrix.append(input_list)

    print(f"#{t} {five_in_row(N, input_matrix)}")
