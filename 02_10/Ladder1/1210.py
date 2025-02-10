# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14ABYKADACFAYh&probBoxId=AZTP3wYKXqbHBIRD&type=PROBLEM&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")


def ladder(matrix):
    pass


for t in range(10):
    N = int(input())
    input_matrix = []
    for n in range(100):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{N} {ladder(input_matrix)}")