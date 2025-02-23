# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV14mbSaAEwCFAYD&solveclubId=AZTP1QzqXnbHBIRD&problemBoxTitle=%2802.17%29+Stack2-1&problemBoxCnt=5&probBoxId=AZTP3wYKXqvHBIRD

import sys
sys.stdin = open("input.txt")


def calculator(size, string):
    stack = [""] * size
    top = -1
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for n in string:
        if n in numbers:
            top += 1
            stack[top] = int(n)
            if stack[top-1] == "+":
                result = stack[top - 2] + stack[top]
                top -= 2
                stack[top] = result
        else:
            top += 1
            stack[top] = n

    return stack[top]


for t in range(1, 11):
    N = int(input())
    expression = input()
    print(f"#{t} {calculator(N, expression)}")
