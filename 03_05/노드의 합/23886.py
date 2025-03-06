# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkJXjKCHvHBINE&probBoxId=AZVjg-a6ABHHBITD&type=USER&problemBoxTitle=%2803.05%29+tree2&problemBoxCnt=3

import sys
sys.stdin = open("5178_input.txt")


T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(M)]

    bin_tree = [0] * (N + 1)  # 이진트리 저장할 배열

    for row in matrix:
        bin_tree[row[0]] = row[1]  # 리프 노드 저장

    idx = N  # 마지막 리프 노드부터 시작

    if N % 2 == 0:  # 만약 마지막 리프노드가 부모노드와 혼자 연결되어 있다면 혼자 반영
        bin_tree[idx // 2] = bin_tree[idx]
        idx -= 1

    while idx > 1:
        bin_tree[idx // 2] = bin_tree[idx] + bin_tree[idx - 1]  # 부모노드 = 자식노드 둘의 합
        idx -= 2

    print(f"#{t} {bin_tree[L]}")
