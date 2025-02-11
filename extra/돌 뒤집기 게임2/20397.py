# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AY3o7m4axawDFAUZ

import sys
sys.stdin = open("sample_in.txt", "r")


def flip_rock(rocks, matrix):
    for row in matrix:
        for i in range(1, row[1]+1):
            if row[0] - 1 - i >= 0 and row[0] - 1 + i < len(rocks):         # 기준이 되는 돌 기준으로 범위 안에 있는 돌만
                if rocks[row[0] - 1 - i] == rocks[row[0] - 1 + i]:          # 인덱스 = row[0] - 1
                    if rocks[row[0] - 1 - i] == 1:
                        rocks[row[0] - 1 - i] = 0
                        rocks[row[0] - 1 + i] = 0
                    else:
                        rocks[row[0] - 1 - i] = 1
                        rocks[row[0] - 1 + i] = 1
    return "".join(rocks)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_matrix = []
    for m in range(M):
        _, __ = map(int, input().split())
        input_matrix.append([_, __])

    print(f"#{t} {flip_rock(input_list, input_matrix)}")
