# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV7GLXqKAWYDFAXB&probBoxId=AZT4yWiKS8vHBIOK&type=PROBLEM&problemBoxTitle=IM+%EB%8C%80%EB%B9%84%ED%95%98%EC%9E%90%21&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")


def harvest(size, matrix):
    total_money = 0
    middle = size // 2

    # i가 커지면서 middle에 가까워지다가 다시 멀어지는 점 이용
    for i in range(size):
        if i <= middle:                                          # 내려가면서 범위가 넓어지는 동안
            for money in matrix[i][middle-i:middle+i+1]:         # 수확할 구간은 middle - i ~ middle + i
                total_money += money

        else:                                                    # 내려가면서 범위가 줄어드는 구간
            for money in matrix[i][i - middle:size-(i-middle)]:  # 수확할 구간은 i - middle ~ size - (i-middle)
                total_money += money

    return total_money


T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_matrix = []
    for r in range(N):
        input_list = list(map(int, input()))
        input_matrix.append(input_list)

    print(f"#{t} {harvest(N, input_matrix)}")
