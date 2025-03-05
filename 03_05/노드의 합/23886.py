# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkJXjKCHvHBINE&probBoxId=AZVjg-a6ABHHBITD&type=USER&problemBoxTitle=%2803.05%29+tree2&problemBoxCnt=3

import sys
sys.stdin = open("5178_input.txt")


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(M)]

    bin_tree = [0]*(N+1)

    for row in matrix:
        bin_tree[row[0]] = row[1]

    idx = N

    if N % 2 == 1:


    else:
        bin_tree[idx//2] = bin_tree[idx]

