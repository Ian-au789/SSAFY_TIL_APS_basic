# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PuPq6AaQDFAUq&probBoxId=AZTP3wYKXqXHBIRD&type=PROBLEM&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

import sys
sys.stdin = open("input.txt", "r")


def find_location(puzzle_size, word_length, matrix):
    cnt = 0

    for search in range(2):
        # 행 탐색
        for row in matrix:
            for i in range(puzzle_size - word_length + 1):                    # 탐색 범위 벗어나지 않게 범위 조절

                if sum(row[i:i+word_length]) == word_length:                  # 단어 길이만큼 슬라이싱한 리스트가 전부 1로 채워저 있는지 확인
                    if i == 0 and row[i+word_length] == 0:                    # 1. 단어가 맨 앞에 있고 바로 다음 항목이 0
                        cnt += 1

                    elif i == puzzle_size - word_length and row[i-1] == 0:    # 2. 단어가 맨 뒤에 있고 바로 앞 항목이 0
                        cnt += 1

                    elif row[i-1] == 0 and row[i+word_length] == 0:           # 3. 단어 앞 뒤 항목이 0
                        cnt += 1

        # 전치 2번 방지
        if search == 1:
            break

        # 전치 행렬 (행과 열 바꿔서 행 탐색 코드 그대로 열 탐색)
        for i in range(puzzle_size):
            for j in range(puzzle_size):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return cnt


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    input_matrix = []

    for n in range(N):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{t} {find_location(N, K, input_matrix)}")