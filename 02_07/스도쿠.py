# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5Psz16AYEDFAUq&probBoxId=AZTP3wYKXqXHBIRD&type=PROBLEM&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

import sys
sys.stdin = open("input.txt", "r")


def check_sudoku(matrix):
    check_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}                # 숫자가 1부터 9까지 안 겹치고 들어있나 확인

    for i in range(9):
        check_row = set()                                  # 행과 열 확인용 집합, 반복마다 초기화
        check_column = set()

        for j in range(9):
            check_row.add(matrix[i][j])
            check_column.add(matrix[j][i])

        if check_row != check_set or check_column != check_set:    # check_set 와 일치하지 않으면 0 반환
            return 0

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:                             # 3칸마다 나눠서 확인
            check_box = set()
            for di in range(3):                         # 3*3 상자 확인
                for dj in range(3):
                    check_box.add(matrix[i+di][j+dj])

            if check_box != check_set:                  # 확인 후 불일치 하면 0 반환
                return 0

    return 1                                            # 모든 항목 확인했으면 1 반환


T = int(input())
for t in range(1, T+1):
    input_matrix = []

    for n in range(9):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{t} {check_sudoku(input_matrix)}")