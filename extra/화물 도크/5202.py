# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZT4zs56TIvHBIOK&probBoxId=AZT4yWiKS8vHBIOK&type=USER&problemBoxTitle=IM+대비하자%21&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")


def max_truck(plan):
    pass


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        operation = list(map(int, input().split()))
        arr.append(operation)

    print(f"{t} {max_truck(arr)}")