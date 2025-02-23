# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZFI63Qa8aQDFAVs&probBoxId=AZTP3wYKXq3HBIRD&type=USER&problemBoxTitle=%2802.19%29+Queue-1&problemBoxCnt=6

import sys
sys.stdin = open("5097_input.txt")


def rotation(size, trial):
    return trial % size


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    print(f"#{t} {numbers[rotation(N, M)]}")
