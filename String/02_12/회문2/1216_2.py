# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14Rq5aABUCFAYi&probBoxId=AZTP3wYKXqjHBIRD&type=PROBLEM&problemBoxTitle=%2802.12%29+String-2&problemBoxCnt=4

import sys
sys.stdin = open("input.txt", "r")


def palindrome(matrix):
    for length in range(100, 0, -1):                         # 회문 길이 100부터 1까지 탐색

        for row in matrix:                                   # 행 탐색
            for i in range(101-length):                      # 탐색 시작 위치

                for j in range(length//2):                   # 회문 확인
                    if row[i+j] != row[i+length-1-j]:
                        break

                    if j == length//2 - 1:
                        return length

        for c in range(100):                                 # 열 탐색
            for i in range(101-length):
                for j in range(length//2):
                    if matrix[i+j][c] != matrix[i+length-1-j][c]:
                        break

                    if j == length//2 - 1:
                        return length

    return -1


for t in range(10):
    T = int(input())
    input_matrix = []

    for _ in range(100):
        input_list = list(input())
        input_matrix.append(input_list)

    print(f"#{T} {palindrome(input_matrix)}")
