# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkGqxaBzLHBINE&probBoxId=AZVjg-a6ABDHBITD&type=USER&problemBoxTitle=%2803.04%29+tree1&problemBoxCnt=4

import sys
sys.stdin = open("input(15).txt")


def in_order(n):
    check = 0
    for k in range(len(vertex[n])):
        if vertex[n][k] == 1:
            in_order(k)
            check += 1
            if check == 1:                     # 자식 1번 순회하고 프린트
                phrase.append(node_number[n])

    else:
        if check == 0:                        # 더 이상 자식이 없는 리프 노드이면 프린트
            phrase.append(node_number[n])
            return


for t in range(1, 11):
    N = int(input())
    nodes = [list(map(str, input().split()))for _ in range(N)]
    vertex = [[0]*(N+1) for _ in range(N+1)]

    node_number = {}
    for row in nodes:
        if len(row) == 2:
            pass

        elif len(row) == 3:
            vertex[int(row[0])][int(row[2])] = 1

        else:
            vertex[int(row[0])][int(row[2])] = 1
            vertex[int(row[0])][int(row[3])] = 1

        node_number[int(row[0])] = row[1]

    phrase = []
    in_order(1)
    p = "".join(phrase)
    print(f"#{t} {p}")
