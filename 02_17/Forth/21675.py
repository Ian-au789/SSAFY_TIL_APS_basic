# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEvJfCqa1MDFAVs&probBoxId=AZTP3wYKXqvHBIRD&type=USER&problemBoxTitle=%2802.17%29+Stack2-1&problemBoxCnt=5

import sys
sys.stdin = open("4874_input.txt")


def forth_calculator(formula):
    stack = [""] * len(formula)
    top = -1
    weight = {1: ["+", "-"], 2: ["*", "/"]}

    for n in formula:
        if n in weight[1]:
            if type(stack[top]) == int and type(stack[top-1]) == int:
                if n == "+":
                    value = stack[top] + stack[top-1]
                    top -= 1
                    stack[top] = value
                else:
                    value = stack[top - 1] - stack[top]
                    top -= 1
                    stack[top] = value

            else:
                return "error"

        elif n == ".":
            return stack[top]

        elif n in weight[2]:
            if type(stack[top]) == int and type(stack[top-1]) == int:
                if n == "*":
                    value = stack[top] * stack[top-1]
                    top -= 1
                    stack[top] = value
                else:
                    value = stack[top - 1] // stack[top]
                    top -= 1
                    stack[top] = value

            else:
                return "error"

        else:
            top += 1
            stack[top] = int(n)


T = int(input())
for t in range(1, T+1):
    expression = list(map(str, input().split()))
    print(f"#{t} {forth_calculator(expression)}")
