# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PobmqAPoDFAUq&probBoxId=AZTP3wYKXqbHBIRD&type=PROBLEM&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")


def snail_matrix(size):
    snail = [[0]*size for _ in range(size)]     # 0만 들어있는 달팽이 생성
    row, col = 0, 0
    number = 1

    snail[row][col] += number                   # 출발점에서 번호 더하고 시작

    while number < size**2:                     # number가 최댓값에 도달할 때 까지
    # 다음 향할 항목의 인덱스가 범위 내에 있고 비어 있으면 좌표 이동, 숫자 + 1한 뒤 숫자 할당
        while col + 1 < size and snail[row][col+1] == 0:
            col += 1
            number += 1
            snail[row][col] += number

        while row + 1 < size and snail[row+1][col] == 0:
            row += 1
            number += 1
            snail[row][col] += number

        while col - 1 >= 0 and snail[row][col-1] == 0:
            col -= 1
            number += 1
            snail[row][col] += number

        while row - 1 >= 0 and snail[row-1][col] == 0:
            row -= 1
            number += 1
            snail[row][col] += number

        continue

    for s in snail:
        print(" ".join(map(str, s)))


T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f"#{t}")
    snail_matrix(N)
