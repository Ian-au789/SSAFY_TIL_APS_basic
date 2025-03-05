# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkHs06B73HBINE&probBoxId=AZVjg-a6ABDHBITD&type=USER&problemBoxTitle=%2803.04%29+tree1&problemBoxCnt=4

import sys
sys.stdin = open("5174_input.txt")


def subtree(n):
    cnt = 0
    for i in range(len(vertex[n])):
        if vertex[n][i]:
            cnt += 1
            cnt += subtree(i)
    else:
        return cnt


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    m = max(nodes)

    vertex = [[0]*(m+1) for _ in range(m+1)]
    for i in range(len(nodes)//2):
        vertex[nodes[i*2]][nodes[i*2+1]] = 1

    print(f"#{t} {subtree(N) + 1}")
