# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkIqqaCD7HBINE&probBoxId=AZVjg-a6ABHHBITD&type=USER&problemBoxTitle=%2803.05%29+tree2&problemBoxCnt=3

import sys
sys.stdin = open("input(16).txt")


for t in range(1, 11):
    N = int(input())
    nodes = [list(map(str, input().split())) for _ in range(N)]

    numbers = {}
    operators = []

    for node in nodes:
        if len(node) == 4:
            operators.append([int(node[0]), node[1], (int(node[2]), int(node[3]))])
        else:
            numbers[int(node[0])] = int(node[1])

    idx = 0
    while len(operators) > 0:
            if operators[idx][2][0] in numbers and operators[idx][2][1] in numbers:
                if operators[idx][1] == "+":
                    result = numbers[operators[idx][2][0]] + numbers[operators[idx][2][1]]

                elif operators[idx][1] == "-":
                    result = numbers[operators[idx][2][0]] - numbers[operators[idx][2][1]]

                elif operators[idx][1] == "*":
                    result = numbers[operators[idx][2][0]] * numbers[operators[idx][2][1]]

                elif operators[idx][1] == "/":
                    result = numbers[operators[idx][2][0]] // numbers[operators[idx][2][1]]

                numbers[operators[idx][0]] = result
                operators.pop(idx)

            idx += 1
            if idx >= len(operators):
                idx = 0

    print(f"#{t} {result}")





