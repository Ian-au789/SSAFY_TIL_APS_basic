# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14nnAaAFACFAYD&probBoxId=AZTP3wYKXqzHBIRD&type=PROBLEM&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

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
            if stack[top - 1] == "*":
                mult = stack[top - 2] * stack[top]
                top -= 2
                stack[top] = mult
        else:
            top += 1
            stack[top] = n

    while top > 0:
        if stack[top] == "+":
            added = stack[top -1] + stack[top + 1]
            top -= 1
            stack[top] = added

        else:
            top -= 1

    return stack[top]



for t in range(1, 11):
    N = int(input())
    expression = input()
    print(f"#{t} {calculator(N, expression)}")
