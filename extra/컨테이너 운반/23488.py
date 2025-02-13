# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZT4zC2qTCrHBIOK&probBoxId=AZT4yWiKS8vHBIOK&type=USER&problemBoxTitle=IM+%EB%8C%80%EB%B9%84%ED%95%98%EC%9E%90%21&problemBoxCnt=6

import sys
sys.stdin = open("sample_input(3).txt", "r")


def shipping(cargo, truck, weight_list, capacity_list):
    pass


T = int(input())
for t in range(1, T+1):
    N, M = int(input().split())
    list_N = list(map(int, input().split()))
    list_M = list(map(int, input().split()))

    print(f"#{t} {shipping(N, M, list_N, list_M)}")
