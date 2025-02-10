# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5Pq-OKAVYDFAUq&probBoxId=AZTP3wYKXqbHBIRD&type=PROBLEM&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")


def matrix_rotation(size, matrix):
    for i in range(size):
        for j in range(size):
            print(matrix[size-1-j][i], end='')                  # [size-1][0] 부터 위로 올라가기
        print(" ", end='')

        for j in range(size):
            print(matrix[size - 1 - i][size - 1 - j], end='')   # [size-1][size-1] 부터 왼쪽으로 읽기
        print(" ", end='')

        for j in range(size):
            print(matrix[j][size-1-i], end='')                  # [0][size-1] 부터 아래로 내려가기
        print("")


T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_matrix = []
    for n in range(N):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{t}")
    matrix_rotation(N, input_matrix)
