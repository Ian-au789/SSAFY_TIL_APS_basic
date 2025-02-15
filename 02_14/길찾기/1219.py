# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14geLqABQCFAYD&probBoxId=AZTP3wYKXqrHBIRD&type=PROBLEM&problemBoxTitle=%2802.14%29+Stack1-2&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")


def check_route():
    # 스택 준비
    top = -1
    stack = [0]*100
    visited = [0]*101

    # 시작점 0
    top += 1
    stack[top] = 0
    visited[0] = 1

    while 1:
        for v in routes[stack[top]]:
            if visited[v] == 0:
                if v == 99:
                    return 1

                top += 1
                stack[top] = v
                visited[v] = 1
                break

            else:
                continue

        else:
            top -= 1

            if top == -1:
                return 0


for t in range(10):
    test_case, route_num = map(int, input().split())
    input_list = list(map(int, input().split()))

    routes = [[] for _ in range(100)]

    idx = 0
    while idx < route_num*2:
        routes[input_list[idx]].append(input_list[idx + 1])
        idx += 2

    print(f"#{test_case} {check_route()}")
