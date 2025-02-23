# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWVWgkP6sQ0DFAUO&probBoxId=AZTP3wYKXqfHBIRD&type=PROBLEM&problemBoxTitle=%2802.11%29+String-1&problemBoxCnt=7

import sys
sys.stdin = open("sample_input.txt", "r")


def read_vertical(matrix):
    size = 0
    for row in matrix:
        if size < len(row):
            size = len(row)                   # 가장 길이가 긴 리스트 찾기

    for row in matrix:
        while len(row) < size:
            row.append(" ")                   # 가장 긴 리스트에 맞춰 다른 리스트에 " " 추가(공란)

    read = []
    for i in range(size):
        for j in range(5):
            if matrix[j][i] != " ":           # 세로로 탐색하면서 공란이 아니면 read 리스트에 더하기
                read.append(matrix[j][i])

    return "".join(read)


T = int(input())
for t in range(1, T+1):
    input_matrix = []
    for _ in range(5):
        input_list = list(input())
        input_matrix.append(input_list)

    print(f"#{t} {read_vertical(input_matrix)}")
