# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PobmqAPoDFAUq&probBoxId=AZTP3wYKXqbHBIRD&type=PROBLEM&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")


def snail_matrix(size):
    snail = [[0]*size for _ in range(size)]     # 0만 들어있는 달팽이 생성
    row, col = 0, 0
    number = 1
    snail[row][col] += number

    for number in range(1, size**2+1):
        snail[row][col] += number

        if 0 <= col + 1 < size:
            if snail[row][col + 1] == 0:
                col += 1
                continue

        if 0 <= row + 1 < size:
            if snail[row + 1][col] == 0:
                row += 1
                continue

        if 0 <= col - 1 < size:
            if snail[row][col - 1] == 0:
                col -= 1
                continue

        if 0 <= row - 1 < size:
            if snail[row - 1][col] == 0:
                row -= 1
                continue

    for s in snail:
        print(" ".join(map(str, s)))


T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f"#{t}")
    snail_matrix(N)
