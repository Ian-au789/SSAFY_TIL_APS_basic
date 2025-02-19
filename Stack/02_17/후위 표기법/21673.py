# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEvIlpKa0IDFAVs&probBoxId=AZTP3wYKXqvHBIRD&type=USER&problemBoxTitle=%2802.17%29+Stack2-1&problemBoxCnt=5

import sys
sys.stdin = open("calc_input.txt")


def back_expression(formula):
    top = -1
    stack = [0]*len(formula)
    new_formula = []

    weight = {0: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 1: ["+", "-"], 2: ["*", "/"]}

    for i in range(len(formula)):
        if formula[i] in weight[0]:
            new_formula.append(formula[i])

        elif formula[i] in weight[1]:
            if stack[top] in weight[2]:
                new_formula.append(stack[top])
                top -= 1

            top += 1
            stack[top] = formula[i]

        else:
            if stack[top] in weight[2]:
                new_formula.append(stack[top])
                top -= 1

            top += 1
            stack[top] = formula[i]

    while top > -1:
        new_formula.append(stack[top])
        top -= 1

    return "".join(new_formula)


T = int(input())
for t in range(1, T+1):
    case = input()
    print(f"#{t} {back_expression(case)}")
