# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEk40hq-AcDFAVs&probBoxId=AZTP3wYKXqnHBIRD&type=USER&problemBoxTitle=%2802.13%29+Stack1-1&problemBoxCnt=5

import sys
sys.stdin = open('bracket_input.txt')


def check_bracket(brackets):
    top = -1
    size = len(brackets)
    stack = [0]*size

    for i in range(size):
        if brackets[i] == "(":
            top += 1
            if top == size:
                return -1
            else:
                stack[top] = "("

        elif brackets[i] == ")":
            if top == -1:
                return -1
            else:
                top -= 1

    if top == -1:
        return 1
    else:
        return -1


T = int(input())
for t in range(1, T+1):
    input_list = list(input())
    print(f"#{t} {check_bracket(input_list)}")
