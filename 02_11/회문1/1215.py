# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14QpAaAAwCFAYi&probBoxId=AZTP3wYKXqfHBIRD&type=PROBLEM&problemBoxTitle=%2802.11%29+String-1&problemBoxCnt=7

import sys
sys.stdin = open("input.txt", "r")


def palindrome(length, matrix):
    cnt = 0

    for trial in range(2):                                       # 전치 행렬 한 후 한번 더 탐색
        for row in matrix:                                       # 행 탐색
            for i in range(9 - length):

                check = 0
                for j in range(length//2):                       # 회문 확인
                    if row[i+j] == row[i+length-1-j]:
                        check += 1
                if check == length//2:                           # 회문 확인할 때 마다 카운트
                    cnt += 1

        for m in range(8):
            for n in range(8):
                if m < n:
                    matrix[m][n], matrix[n][m] = matrix[n][m], matrix[m][n]

    return cnt


for t in range(1, 11):
    N = int(input())
    input_matrix = []
    for _ in range(8):
        input_list = list(input())
        input_matrix.append(input_list)

    print(f"#{t} {palindrome(N, input_matrix)}")
