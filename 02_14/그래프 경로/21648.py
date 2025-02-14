# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEqAGXqvIcDFAVs&probBoxId=AZTP3wYKXqrHBIRD&type=USER&problemBoxTitle=%2802.14%29+Stack1-2&problemBoxCnt=5

import sys
sys.stdin = open("4871_input.txt")


def graph_edge(num_v, num_e, v_s, v_e, edge_list):

    top = -1
    stack = [""]*num_e
    visited = [""]*num_v

    top += 1
    stack[top] = v_s
    visited[0] = v_s

    while top >= 0:

        for idx in range(num_e):
            if stack[top] in edge_list[idx]:

                for v in edge_list[idx]:
                    if v not in visited and v != stack[top]:
                        top += 1
                        stack[top] = v

                        if stack[top] == v_e:
                            return 1

                        break

            if idx == num_e - 1:
                top -= 1

    return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    input_list = []

    for _ in range(E):
        v1, v2 = map(int, input().split())
        input_list.append([v1, v2])

    start, end = map(int, input().split())
    print(f"#{t} {graph_edge(V, E, start, end, input_list)}")
