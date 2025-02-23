# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV13_BWKACUCFAYh&probBoxId=AZTP3wYKXqXHBIRD&type=PROBLEM&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

import sys
sys.stdin = open("input.txt", "r")


def find_largest(matrix):
    maximum = 0

    diagonal_1 = 0
    diagonal_2 = 0

    for i in range(100):
        row = sum(matrix[i])                    # 행의 합
        if maximum < row:
            maximum = row

        column = 0
        for j in range(100):
            column += matrix[j][i]              # 열의 합

        if maximum < column:
            maximum = column

        diagonal_1 += matrix[i][i]              # 대각선 2개

        diagonal_2 += matrix[i][99-i]

    return max(maximum, diagonal_1, diagonal_2)


for test in range(10):
    T = int(input())
    input_matrix = []

    for n in range(100):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{T} {find_largest(input_matrix)}")
